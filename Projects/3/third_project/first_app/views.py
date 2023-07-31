from django.shortcuts import render

# Create your views here.

def contact(request):
    
    # return render(request, './first_app/index.html', context = {'author': 'Phitron', 'age': 13}
        

    # return render(request, './first_app/index.html', {'courses': [
    # {
    #     'id': 1,
    #     'course': 'A',
    #     'teacher': 'Nayeem'
    # },
    # {
    #     'id': 2,
    #     'course': 'B',
    #     'teacher': 'Bayeem'
    # },
    # {
    #     'id': 3,
    #     'course': 'C',
    #     'teacher': 'Cayeem'
    # },
    # ]}
    # )

        return render(request, './first_app/index.html', {"name": "I am Nayeem", "marks": 86, "lst": [24, 3, 10, 5], "blog": "loremkjkldjfkl dsjfeiwhfjdkisjvlcdvm dokfjdk  dfkdjskf dfkom df dlkfdls "})