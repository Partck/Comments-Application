comments = []

class Comments:

	def __init__(self):
		self.db = comments


	def create_comments(self, message, author):

		payload = {
			"id": len(self.db)+1,
			"message": message,
			"author": author
		}
		self.db.append(payload)
		return payload

	def edit_comment(self, commentsid, newmessage):
		edit_comment = [comm for comm in self.db if comm['id'] == commentsid]
		if edit_comment:
			edit_comment[0]['message'] = newmessage
			return edit_comment
		else:
			return False
	
