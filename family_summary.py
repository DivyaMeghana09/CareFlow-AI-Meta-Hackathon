
def generate_family_summary(client, memories):
    if not memories:
        return "No care observations have been recorded yet."

    dated_memories = [
        item for item in memories
        if item.get("date") and item.get("observation")
    ]

    if not dated_memories:
        return "No dated care observations are available."

    latest_date = max(item["date"] for item in dated_memories)

    recent = [
        item for item in dated_memories
        if item["date"] == latest_date
    ]

    # Remove duplicate observations.
    unique = []
    seen = set()

    for item in recent:
        observation = item["observation"].strip()
        mood = item.get("mood", "not recorded")
        key = (observation.casefold(), mood.casefold())

        if key not in seen:
            seen.add(key)
            unique.append(item)

    bullets = []

    for item in unique[-5:]:
        observation = item["observation"].strip()
        mood = item.get("mood", "not recorded")

        bullets.append(
            f"- {observation} (Reported mood: {mood})"
        )

    return (
        f"Family Care Summary — {latest_date}\n\n"
        + "\n".join(bullets)
        + "\n\nCaregiver follow-up: Review these observations "
          "and contact the appropriate care professional "
          "when concerns require attention."
    )
