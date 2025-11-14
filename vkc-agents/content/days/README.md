# Day-level Packaging (Days 01–28)

Each `dayNN/manifest.json` points to the canonical assets without duplicating files.
Use this when uploading in Atlas so you can click through and copy the right files fast.

Fields
- week: 1..4
- theme: short mnemonic for the day
- shorts_srt: path to KR/VI subtitles
- card_csv: path to 5-slide Cardnews CSV
- captions: path to KR/VI channel captions
- checklist: path to day publish checklist

For the full list, see `content/upload_schedule.csv`.
