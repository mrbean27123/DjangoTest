from django.shortcuts import render


def main(request):
    data = {
        "title": "Main page",
        "values": [
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit.Eius, sequi."
            "Lorem ipsum dolor sit amet, consectetur adipisicing elit.Ad animi blanditiis eveniet fuga, odio tempora."
            "Lorem ipsum dolor sit amet."
            "Lorem ipsum dolor sit amet, consectetur adipisicing."
            "Lorem ipsum dolor."
            "Lorem ipsum. "
        ],
        "obj": {
            "title": "Django",
            "description": "Lorem ipsum dolor sit amet",
            "date": None,
            "time": None,
        }
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        "title": "About page",
        "values": ["hello", "world", "hello", "world"],
    }
    return render(request, 'main/about.html', data)
