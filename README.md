# LiveKit SIP Integration

This repository contains the configuration and setup for LiveKit SIP integration with Twilio. It includes inbound trunk configuration and dispatch rules for handling incoming calls.

## Configuration Files

### Inbound Trunk Configuration (`inbound-trunk.json`)
- Configures the inbound trunk for accepting calls from Twilio
- Uses Krisp noise cancellation
- Handles the Kingsburg phone number (+1-559-238-0249)

### Dispatch Rule Configuration (`dispatch-rule.json`)
- Creates individual rooms for each caller
- Room names are prefixed with "call-kingsburg-"
- Dispatches an inbound agent to each new room
- Includes metadata for job dispatch

## Main Application (`main.py`)
The main application uses:
- Groq for Speech-to-Text
- Google's Gemini 2.0 Flash for LLM
- ElevenLabs for Text-to-Speech
- Silero for Voice Activity Detection
- Multilingual Turn Detection

## Setup
1. Install dependencies:
```bash
pip install \
  "livekit-agents[deepgram,google,elevenlabs,groq,openai,cartesia,silero,turn-detector]~=1.0" \
  "livekit-plugins-noise-cancellation~=0.2" \
  "python-dotenv"
```

2. Set up environment variables in `.env`

3. Download required model files:
```bash
python main.py download-files
```

4. Run the application:
```bash
python main.py
```

## LiveKit Configuration
- SIP Trunk ID: ST_c36DrVRC2Wj7
- Dispatch Rule ID: SDR_cdvkeFCv2556

## Security Note
This repository uses environment variables for sensitive configuration. Make sure to properly set up your `.env` file and never commit it to version control. 