
class RequestUser:
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
