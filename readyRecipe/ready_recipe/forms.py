from django import forms
from django.forms import ModelForm
from ready_recipe.models import Category,Recipe,Comment,UserProfile
from django.contrib.auth.models import User
import datetime


class RecipeForm(forms.ModelForm):
    DIFFICULTY = ( ('1','1'),('2','2' ),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10') )
    PORTIONS = ( ('1','1'),('2','2' ),('3','3'),('4','4'),('5','5'),('6','More than 5') )
    TIME_NEEDED = ( ('1','1-15 minutes'),('2','15-30 minutes' ),('3','30-60 minutes'),('4','1-1.30 hours'),('5','1.30-2 hours'),('6','2-2.30 hours'),('7','More than 2.30 hours'),)

    name = forms.CharField(max_length=300,help_text = "Recipe Title")
    picture = forms.ImageField(required = False,help_text = 'Photo ')
    instuction = forms.CharField(widget=forms.Textarea,help_text = "Method")
    portions = forms.ChoiceField(choices = PORTIONS,help_text="Portions")
    difficulty = forms.ChoiceField(choices=DIFFICULTY,help_text = 'Difficulty' )
    completion_time = forms.ChoiceField(choices=TIME_NEEDED,help_text = 'Time')  
    calories = forms.IntegerField(help_text = 'Calories per portion')
    ingredients = forms.CharField(widget=forms.Textarea,help_text = "Ingredients")
    average_overall_price = forms.FloatField(help_text = 'Price per portion')
    views = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    owner_id = forms.IntegerField(widget=forms.HiddenInput(),required=False)


    class Meta:
        model = Recipe
        exclude = ('views','slug','owner_id',)

class CommentForm(forms.ModelForm):
    date = forms.DateField(widget=forms.HiddenInput(),required=False,initial=datetime.date.today())
    recommentations = forms.CharField(widget=forms.Textarea,help_text="Add your own Comment")


    class Meta:
        model = Comment
        fields = ('recommentations',)



class UserProfileForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)


    class Meta:
        model = UserProfile
        exclude = ('slug',)




