#!/bin/bash
# Setup Video Editing for the Content Machine
# Run once: bash scripts/setup-video.sh
# Installs Remotion dependencies and downloads the Whisper transcription model.

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT_DIR="$(dirname "$SCRIPT_DIR")"
VIDEO_DIR="$ROOT_DIR/video"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Content Machine — Video Setup"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check for Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is required but not installed."
    echo "   Install it: https://nodejs.org/"
    exit 1
fi

NODE_VERSION=$(node -v | cut -d'v' -f2 | cut -d'.' -f1)
if [ "$NODE_VERSION" -lt 18 ]; then
    echo "❌ Node.js 18+ required. Found: $(node -v)"
    exit 1
fi
echo "✓ Node.js $(node -v)"

# Check for ffmpeg
if ! command -v ffmpeg &> /dev/null; then
    echo "❌ ffmpeg is required but not installed."
    echo "   Install it: brew install ffmpeg (macOS) or apt install ffmpeg (Linux)"
    exit 1
fi
echo "✓ ffmpeg $(ffmpeg -version 2>&1 | head -1 | awk '{print $3}')"

# Install npm dependencies
echo ""
echo "Installing Remotion dependencies..."
cd "$VIDEO_DIR"
npm install
echo "✓ Dependencies installed"

# Download Whisper model for transcription
echo ""
echo "Downloading Whisper transcription model (medium.en)..."
echo "This is ~1.5GB and only needs to happen once."
npx tsx src/lib/transcribe.ts --help 2>/dev/null || true

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Setup complete!"
echo ""
echo "  Preview:    cd video && npm run studio"
echo "  Transcribe: cd video && npm run transcribe audio.wav captions.json"
echo "  Render:     cd video && npm run render CaptionedClip out/clip.mp4"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
