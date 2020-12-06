from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
	def has_object_permission(self,request,view,obj):
		return request.user == obj.author_of_post

class ReadOnly(BasePermission):
    def has_object_permission(self,request,view,obj):
        return request.method == 'GET'

