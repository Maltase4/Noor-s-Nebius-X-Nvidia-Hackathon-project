# A dictionary of category keywords and their recycling guidelines
RECYCLING_RULES = {
    "plastic": "Plastics marked with codes 1 and 2 are widely recyclable. Rinse before tossing. Soft plastics/bags usually require drop-off bins.",
    "cardboard": "Flatten cardboard boxes to save space. Keep them dry and free of heavy food grease (greasy pizza boxes should be composted if possible).",
    "glass": "Glass bottles and jars are infinitely recyclable. Rinse them out. Metal lids go in recycling; corks usually don't.",
    "battery": "Batteries contain hazardous materials and MUST NOT go in regular trash. Take them to a designated e-waste recycling drop-off point.",
    "electronics": "E-waste (phones, chargers, cables) contains toxic metals. Bring them to certified e-waste recycling events or retail drop-offs.",
    "food": "Organic food scraps and waste should go into a compost bin rather than a landfill to reduce methane emissions.",
    "aluminum": "Aluminum cans and foil are 100% recyclable and can be recycled indefinitely. Rinse lightly before binning."
}

def lookup_local_rule(user_query: str) -> str:
    """
    Searches the user's query for category keywords and returns 
    relevant local recycling guidelines, ensuring flexibility.
    """
    query_lower = user_query.lower()
    matched_guidelines = []

    # Check which keywords appear anywhere in the user's sentence/query
    for keyword, guideline in RECYCLING_RULES.items():
        if keyword in query_lower:
            matched_guidelines.append(f"[{keyword.upper()} RULE]: {guideline}")

    # If keywords matched, return them as hints for the AI
    if matched_guidelines:
        return " | ".join(matched_guidelines)
    
    # Flexible fallback if no explicit keywords are found
    return "General Guideline: Check local municipal rules. Clean and dry items before recycling. When in doubt, avoid wishcycling!"