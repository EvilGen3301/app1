from django.shortcuts import render


def catalog(request):
    context = {
        "title": "Home - კატალოგი",
        "goods": [
            {
                "image": "deps/images/goods/set of tea table and three chairs.jpg",
                "name": "ჩაის მაგიდა და სამი სკამი",
                "description": "სამი სკამის კომპლექტი და დიზაინერი მაგიდა მისაღები ოთახისთვის.",
                "price": 150.00,
            },
            {
                "image": "deps/images/goods/set of tea table and two chairs.jpg",
                "name": "ჩაის მაგიდა და ორი სკამი",
                "description": "მაგიდის და ორი სკამის კომპლექტი მინიმალისტურ სტილში.",
                "price": 93.00,
            },
            {
                "image": "deps/images/goods/double bed.jpg",
                "name": "ორკაციანი საწოლი",
                "description": "საწოლი არის ორმაგი თავსახურით და ზოგადად ძალიან ორთოპედიული.",
                "price": 670.00,
            },
            {
                "image": "deps/images/goods/kitchen table.jpg",
                "name": "სამზარეულოს მაგიდა ნიჟარათი",
                "description": "სამზარეულოს სასადილო მაგიდა ჩაშენებული ნიჟარათი და სკამებით.",
                "price": 365.00,
            },
            {
                "image": "deps/images/goods/kitchen table 2.jpg",
                "name": "სამზარეულოს მაგიდა ჩაშენებული",
                "description": "სამზარეულოს მაგიდა ჩაშენებული ღუმელით და ნიჟარათი. ბევრი თარო და მთლიანობაში ლამაზი.",
                "price": 430.00,
            },
            {
                "image": "deps/images/goods/corner sofa.jpg",
                "name": "კუთხის დივანი მისაღები ოთახისთვის",
                "description": "კუთხის დივანი, გარდაიქმნება ორადგილიან საწოლში, იდეალურია მისაღები და სტუმრების გასართობად!",
                "price": 610.00,
            },
            {
                "image": "deps/images/goods/bedside table.jpg",
                "name": "საწოლის მაგიდა",
                "description": "საწოლის მაგიდა ორი უჯრით (ყვავილი არ შედის კომფლეკტში).",
                "price": 55.00,
            },
            {
                "image": "deps/images/goods/sofa.jpg",
                "name": "ჩვეულებრივი დივანი",
                "description": "დივანი ჩვეულებრივი დივანია, აღსაწერი არაფერია.",
                "price": 190.00,
            },
            {
                "image": "deps/images/goods/office chair.jpg",
                "name": "საოფისე სკამი",
                "description": "ჩამომახრჩეთ ვინცხამ...",
                "price": 30.00,
            },
            {
                "image": "deps/images/goods/plants.jpg",
                "name": "მცენარე",
                "description": "არ მოწიოთ!!",
                "price": 10.00,
            },
            {
                "image": "deps/images/goods/flower.jpg",
                "name": "სტილიზებული ყვავილი",
                "description": "დიზაინერი ყვავილი (შესაძლოა ხელოვნური) ინტერიერის გაფორმებისთვის.",
                "price": 15.00,
            },
            {
                "image": "deps/images/goods/strange table.jpg",
                "name": "საწოლის მაგიდა 2",
                "description": "მაგიდა საკმაოდ უცნაურია გარეგნულად, მაგრამ შესაფერისია საწოლის გვერდით დასაყენებლად.",
                "price": 25.00,
            },
        ],
    }
    return render(request, "goods/catalog.html", context)


def product(request):
    return render(request, "goods/product.html")
