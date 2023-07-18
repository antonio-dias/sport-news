

def verify_halftime(comment):
    time = comment.get("time")
    minute = comment.get("minute")
    if comment.get("comment").split()[0] == "Fim":
        time = int(comment.get("time")) + 1
        minute = -1
    return time, minute

def get_current_game_tag(time):
    if time == 3:
        tag_time = "#narration-penalties"
    else:
        tag_time = f"#narration-{time}-half"
    return tag_time