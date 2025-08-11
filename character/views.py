from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from .models import Character, Disc
from .forms import DiscForm
# Create your views here.

class CharacterList(generic.ListView):
    queryset = Character.objects.all()
    template_name = "character/index.html"
    paginate_by = 6

def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    discs = Disc.objects.filter(character=character)[:6]  # Limit to 6 discs
    if request.method == 'POST':
        form = DiscForm(data=request.POST)
        if form.is_valid():
            # Save the new disc with the selected character
            disc = form.save(commit=False)
            disc.user_id = request.user
            disc.character = character  # Assign disc to character
            disc.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Disc Drive saved'
            )
        form = DiscForm()
    
    return render(request, 'character/character_detail.html', {'form': form, 'character': character, 'discs': discs})