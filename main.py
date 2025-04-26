from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    openai,
    cartesia,
    deepgram,
    groq,
    noise_cancellation,
    silero,
    elevenlabs,
    google,
)
from livekit.plugins.turn_detector.multilingual import MultilingualModel

load_dotenv()
from prompt import prompt, first_message

class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions=prompt)


async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession(
        stt=groq.STT(
            model="whisper-large-v3-turbo",
            language="en",
        ),
        llm=google.LLM(
            model="gemini-2.0-flash-exp",
            temperature=0.8,
        ),
        tts=elevenlabs.TTS(
            voice_id="FVQMzxJGPUBtfz1Azdoy",
            model="eleven_multilingual_v2",
            voice_settings=elevenlabs.tts.VoiceSettings(
                stability=0.71,
                similarity_boost=0.5,
                style=0.0,
                use_speaker_boost=True,
                speed=1.1
            )
        ),
        vad=silero.VAD.load(),
        turn_detection=MultilingualModel(),
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await session.generate_reply(
        instructions=first_message
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))