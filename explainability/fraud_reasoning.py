def generate_reason(row):

    reasons = []

    if row.get("burst_score", 0) > 2:
        reasons.append(
            "High burst review activity detected"
        )

    if row.get("avg_similarity", 0) > 0.8:
        reasons.append(
            "Highly repetitive review content"
        )

    if row.get("degree_centrality", 0) > 0.5:
        reasons.append(
            "Suspicious reviewer connectivity"
        )

    if row.get("time_entropy", 0) < 1:
        reasons.append(
            "Highly predictable posting behavior"
        )

    if row.get("night_post", 0) == 1:
        reasons.append(
            "Unusual nighttime review activity"
        )

    if len(reasons) == 0:
        reasons.append(
            "Low fraud indicators detected"
        )

    return reasons