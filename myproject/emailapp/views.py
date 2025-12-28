from django.shortcuts import render


def home(request):
    emails = [
        {
            "title": "Welcome to the Email App",
            "description": "This is the home page of the Email App.",
            "time": "2024/06/15",
            "status": False,
        },
        {
            "title": "Your Weekly Update",
            "description": "Here is what happened this week in your account.",
            "time": "2024/06/14",
            "status": True,
        },
        {
            "title": "Meeting Reminder",
            "description": "Don't forget about your meeting scheduled for tomorrow.",
            "time": "2024/06/13",
            "status": False,
        },
    ]
    return render(request, "home.html", {"emails": emails})
