from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import StudentSerializer
from .models import Student


class StudentApi(APIView):

    # GET
    def get(self, request, pk=None):

        if pk:
            try:
                student = Student.objects.get(pk=pk)
                serializer = StudentSerializer(student)

                return Response(serializer.data, status=status.HTTP_200_OK)

            except Student.DoesNotExist:
                return Response(
                    {"error": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND
                )

        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST
    def post(self, request):

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # PUT
    def put(self, request, pk=None):

        try:
            student = Student.objects.get(pk=pk)

            serializer = StudentSerializer(student, data=request.data)

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Student.DoesNotExist:
            return Response(
                {"error": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND
            )

    # PATCH
    def patch(self, request, pk=None):

        try:
            student = Student.objects.get(pk=pk)

            serializer = StudentSerializer(student, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()

                return Response(serializer.data, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Student.DoesNotExist:
            return Response(
                {"error": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND
            )

    # DELETE
    def delete(self, request, pk=None):

        try:
            student = Student.objects.get(pk=pk)

            student.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except Student.DoesNotExist:
            return Response(
                {"error": "Student Not Found"}, status=status.HTTP_404_NOT_FOUND
            )
