from pyscript import document

# Club data
clubs = {
    "Robotics Club": {
        "Description": "Build and program competitive robots.",
        "Meeting Time": "Tuesdays 3:45–5:30 PM",
        "Location": "Computer Lab",
        "Advisor": "Ms. Carabot",
        "Number of Members": "18",
        "Category": "Academic"
    },
    "Chess Club": {
        "Description": "Strategy practice and tournaments.",
        "Meeting Time": "Thursdays 4–5 PM",
        "Location": "Library Hall",
        "Advisor": "Mr. Wayne",
        "Number of Members": "12",
        "Category": "Strategy"
    },
    "Forensics Society": {
        "Description": "Speech, debate, and public speaking.",
        "Meeting Time": "Mondays 4–5:30 PM",
        "Location": "Room 204",
        "Advisor": "Ms. Dent",
        "Number of Members": "15",
        "Category": "Academic/Communication"
    },
    "Drama Guild": {
        "Description": "Acting, stage design, and production.",
        "Meeting Time": "Wednesdays & Fridays 4–6 PM",
        "Location": "Auditorium",
        "Advisor": "Mr. Crane",
        "Number of Members": "20",
        "Category": "Performing Arts"
    },
    "Gotham Volunteer Corps": {
        "Description": "Community service and charity work.",
        "Meeting Time": "Variable",
        "Location": "Community Office",
        "Advisor": "Mrs. Gordon",
        "Number of Members": "25",
        "Category": "Volunteer/Service"
    }
}

def show(club_name):
    info_box = document.getElementById("club_info_box")

    if club_name in clubs:
        details = clubs[club_name]
        text = f"Club Name: {club_name}\n"
        for k, v in details.items():
            text += f"{k}: {v}\n"
        info_box.innerText = text
    else:
        info_box.innerText = "No information available."

def ROBCLUB(e):
    show("Robotics Club")

def CHESSCLUB(e):
    show("Chess Club")

def FORCLUB(e):
    show("Forensics Society")

def DRAMCLUB(e):
    show("Drama Guild")

def GVCCLUB(e):
    show("Gotham Volunteer Corps")

