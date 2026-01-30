import os
import subprocess
import asyncio
from dotenv import load_dotenv

from livekit import agents
from livekit.agents import (
    AgentSession,
    Agent,
    RoomInputOptions,
    function_tool,
    RunContext,
)

from livekit.plugins.google.beta import realtime as google_realtime
from livekit.plugins import noise_cancellation


# ----------------- ENV SETUP -----------------
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise RuntimeError("GOOGLE_API_KEY not found in .env")


# ----------------- OPEN APP HELPER -----------------
def open_app(cmd: str) -> str:
    cmd = cmd.lower().strip()

    if any(k in cmd for k in ["notepad", "note pad", "notes"]):
        subprocess.Popen("notepad.exe")
        return "Opening Notepad."

    if any(k in cmd for k in ["calculator", "calc"]):
        subprocess.Popen("calc.exe")
        return "Opening Calculator."

    if "word" in cmd:
        subprocess.Popen("start winword", shell=True)
        return "Opening Microsoft Word."

    if "excel" in cmd:
        subprocess.Popen("start excel", shell=True)
        return "Opening Microsoft Excel."

    return "I didn't recognize that application."


# ----------------- AGENT -----------------
class DesktopAssistant(Agent):
    def init(self):
        super().init(
            instructions=(
                "You are Nova, a Windows voice assistant.\n"
                "Open desktop applications when asked.\n"
                "Go to sleep when asked and stop responding.\n"
                "Wake up only when the user says your name."
            )
        )
        self.sleeping = False

    # -------- OPEN APP --------
    @function_tool()
    async def open_desktop_app(self, ctx: RunContext, query: str) -> str:
        if self.sleeping:
            return ""
        return open_app(query)

    # -------- SLEEP / SHUTDOWN --------
    @function_tool()
    async def control_assistant(self, ctx: RunContext, query: str) -> str:
        text = query.lower().strip()

        if any(k in text for k in ["go to sleep", "stop listening", "be quiet"]):
            self.sleeping = True
            return "Okay, I’m sleeping. Say 'Nova' to wake me up."

        if any(k in text for k in ["exit", "quit", "shutdown"]):

            async def shutdown():
                await ctx.wait_for_playout()
                await ctx.session.aclose()

            asyncio.create_task(shutdown())
            return "Shutting down. Goodbye!"

        return ""

    # -------- WAKE UP --------
    @function_tool()
    async def wake_up(self, ctx: RunContext, query: str) -> str:
        if "nova" in query.lower():
            self.sleeping = False
            return "I’m awake. How can I help you?"
        return ""


# ----------------- ENTRYPOINT -----------------
async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    llm = google_realtime.RealtimeModel(
        api_key=GOOGLE_API_KEY,
        model="models/gemini-1.5-pro-realtime",  # ✅ more stable
        voice="Puck",
        temperature=0.3,
    )

    session = AgentSession(llm=llm)

    await session.start(
        room=ctx.room,
        agent=DesktopAssistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    # ⚠️ IMPORTANT:
    # Do NOT call session.generate_reply()
    # Gemini Realtime responds only after user speaks


# ----------------- RUN -----------------
if __name__ == "main":
    agents.cli.run_app(
        agents.WorkerOptions(entrypoint_fnc=entrypoint)
    )