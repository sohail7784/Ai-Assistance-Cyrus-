
from dotenv import load_dotenv
from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
   noise_cancellation,
)
from livekit.plugins import google
from instruction import cyrus_intstruction,session_instruction
from logic import search,todaysdate,current_time,current_year,present_month,yesterdaysdate,tommorowsdate,youtube,weather,email,whatsapp,set_timer,maps,current_location

load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=cyrus_intstruction,
            llm=google.beta.realtime.RealtimeModel(
            voice="Charon",
            temperature=0.8,
        ),
            tools=[
                search,
                youtube,
                email,
                whatsapp,
                maps,
                current_location,
                set_timer,
                weather,
                todaysdate,
                current_time,
                current_year,
                present_month,
                yesterdaysdate,
                tommorowsdate
                ]
        )


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
           video_enabled=True,
           audio_enabled=True,
           noise_cancellation=noise_cancellation.BVC(), 
        ),
    )
    await session.generate_reply(
        instructions=session_instruction
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))