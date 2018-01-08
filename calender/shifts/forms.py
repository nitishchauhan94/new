from django import forms


from .models import shifts


class ShiftForm(forms.ModelForm):
    class Meta:
        model = shifts
        fields = [
            "date",
            "Day",
            "Morning",
            "Evening",
            "General",
            "Planned",
            "Comp_off",
            "Leave"
        ]