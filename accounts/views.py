from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

@api_view(['POST'])
def register_user(request):
    u = request.data.get('username')
    p = request.data.get('password')
    # 检查用户是否存在
    if User.objects.filter(username=u).exists():
        return Response({'status': 'error', 'message': 'User already exists'}, status=400)
    # 创建新用户
    User.objects.create_user(username=u, password=p)
    return Response({'status': 'success', 'message': 'User created'})

@api_view(['POST'])
def login_user(request):
    u = request.data.get('username')
    p = request.data.get('password')
    # 验证账号密码
    user = authenticate(username=u, password=p)
    if user:
        return Response({'status': 'success', 'message': 'Login successful'})
    return Response({'status': 'error', 'message': 'Invalid credentials'}, status=401)