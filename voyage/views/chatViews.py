from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from voyage.models import Discussion, Publication
from voyage.serializers.chatSerializer import ChatSerializer

# Get all discussions
# =======================
@api_view(['GET'])
def dicussions(request):
    chats = Discussion.objects.all()
    serializer = ChatSerializer(chats, many=True) # Many = True, s'il s'agit d'une liste d'éléments
    return Response(serializer.data)

# Get a specific discussion
# ===========================
@api_view(['GET'])
def dicussion(request, pk):
    chat = Discussion.objects.get(id=pk)
    serializer = ChatSerializer(chat, many=False) # Many = False, s'il s'agit d'un élément
    return Response(serializer.data)

# Create a discussion
# =======================
@api_view(['POST'])
def chat_creation(request):
    data = request.data
    try:
        chat = Discussion.objects.create(

            message = data['message'],
            user_id = request.user,
            pub_id = Publication.objects.get(id=data['pub_id'])
        )
        serializer = ChatSerializer(chat, many=False)
        return Response(serializer.data)
    except:
        return Response({'message':"Vérifiez vos informations"}, 400)

# Update a discussion
# =======================
@api_view(['PUT'])
def chat_update(request, pk):
    try:
        chat = Discussion.objects.get(id=pk)
        data = request.data

        if chat:
            chat.message = data["message"]
            chat.save()

            serializer = ChatSerializer(chat, many=False)
            return Response(serializer.data)
    except:
        return Response({'message':"la discussion n'existe pas"}, 404)

# Delete a publication
# =======================
@api_view(['DELETE'])
def del_chat(request, pk):
    try:
        chat = Discussion.objects.get(id=pk)
        if(chat):
            chat.delete()
            return Response('la discussion est supprimée avec succès')
    except:
        return Response({'message':"la discussion n'existe pas"}, 404)