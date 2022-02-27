from rest_framework import serializers
from .models import Quizzes ,  Question, Answer


class QuizSerializer(serializers.ModelSerializer):
	class Meta:
		model = Quizzes
		fields = [
		'title'
		]


class AnsweSerializer(serializers.ModelSerializer):
	class Meta:
			model = Answer
			fields = [
			# 'question',
			'answer_text',
			'is_right'
			]

class  RandomQuestionSerializer(serializers.ModelSerializer):

	answer = AnsweSerializer(many = True, read_only= True)
	
	class Meta:
		model = Question
		fields = [
		'title', 'answer'
		]


class QuestionSerializer(serializers.ModelSerializer):
	answer = AnsweSerializer(many = True, read_only= True)
	quiz = QuizSerializer(read_only= True)
	class Meta:
		model = Question
		fields = [
		'quiz','title', 'answer'
		]

