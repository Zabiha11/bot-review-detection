def generate_explanation(data):

    reasons = []

    if data.get("burst_score", 0) > 2:
        reasons.append(
            "Burst review activity detected"
        )

    if data.get("avg_similarity", 0) > 0.8:
        reasons.append(
            "Highly repetitive review text"
        )

    if data.get("degree_centrality", 0) > 0.5:
        reasons.append(
            "Reviewer connected to suspicious network"
        )

    if data.get("time_entropy", 0) < 1:
        reasons.append(
            "Predictable posting behavior"
        )

    if data.get("night_post", 0) == 1:
        reasons.append(
            "Nighttime review activity detected"
        )

    if len(reasons) == 0:
        reasons.append(
            "Low fraud indicators"
        )

    return reasons
