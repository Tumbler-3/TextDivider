from django.shortcuts import render
from apps.Divider.forms import ImageForm
from apps.Divider.models import ImageModel
from apps.extractor.extract import extract_word, extract_letters
from apps.recog.recog import recog


def main(request):
    if request.method == 'GET':
        form = ImageForm()
        return render(request, 'main.html', context={'form': form, 'image': None, 'text': None})

    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            words = []
            letters = []
            img = ImageModel.objects.create(img=form.cleaned_data['img'])
            text = extract_word(name=img.img.name, itr=1)
            print(text)
            
            flat_words = []
            for row in text:
                for word in row:
                    flat_words.append(word)
                    
            for w_index, word in enumerate(flat_words, start=1):
                l = extract_letters(word, w_index=w_index)
                letters.append(l)
            print(letters)
            
            
            for row in letters:
                rows = []
                for word in row:
                    w = recog(f"{word}")
                    rows.append(w)
                words.append(rows)
                
            

            return render(request, 'main.html', context={'form': form, 'image': img.img, 'text': text, 'letters':letters, 'words':words })

        return render(request, 'main.html', context={'form': ImageForm(), 'image': None, 'text': None})
