#!/bin/bash

# Daily Oracle - Content Spike Scanner
# Runs the Content Machine Oracle to find content spikes from the last 24 hours
# Posts digest to the configured Oracle channel automatically
#
# Setup: Update config.md with your Slack User ID and Oracle Channel
# Add to crontab: 0 9 * * * /path/to/content-machine/scripts/daily-oracle.sh >> /path/to/content-machine/oracle-reports/cron.log 2>&1

set -e

# Configuration — resolve paths relative to this script
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
OUTPUT_DIR="$PROJECT_DIR/oracle-reports"
DATE=$(date +%Y-%m-%d)
OUTPUT_FILE="$OUTPUT_DIR/oracle-$DATE.md"

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Run the Oracle via Claude CLI
# The --daily flag tells the Oracle to:
# 1. Scan last 24 hours only
# 2. Auto-post digest to the Oracle channel configured in config.md
cd "$PROJECT_DIR"

claude --print "/content-machine --oracle --daily" 2>&1 | tee "$OUTPUT_FILE"

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Oracle complete: $DATE"
echo "Report saved: $OUTPUT_FILE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
