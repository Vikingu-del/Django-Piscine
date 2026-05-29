from django.shortcuts import render


# Create your views here.
def table(request):
    # We create a range of 50 steps.
    # Each step will represent an increase in 'lightness'
    # 255 / 50 is roughly 5.
    shades = []
    for i in range(50):
        intensity = i * 5
        shades.append(intensity)

    return render(request, "ex03/table.html", {"shades": shades})
