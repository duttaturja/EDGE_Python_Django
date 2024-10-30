from django.shortcuts import render, redirect
# Create your views here.

from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.decorators import permission_required

#own
#from user.serializers import CustomClaimTokenObtainSerializer

#rest framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "Logged out successfully"}, status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "Invalid token"}, status=status.HTTP_400_BAD_REQUEST)


def profile_view(request):
    #template_name = 'profile_view.html'
    return render(request, 'profile_view.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
    


