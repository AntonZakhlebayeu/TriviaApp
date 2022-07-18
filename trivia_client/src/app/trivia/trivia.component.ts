import {Component, OnInit} from '@angular/core';
import {TriviaService} from "../trivia.service";
import {Answer, Question, QuestionArray} from "../trivia";
import {MatRadioChange} from "@angular/material/radio";
import {first} from "rxjs/operators";

@Component({
  selector: 'app-trivia',
  templateUrl: './trivia.component.html',
  styleUrls: ['./trivia.component.css']
})
export class TriviaComponent implements OnInit {
  triviaData: QuestionArray = [];
  question: Question|null = null;
  answer: Answer|null = null;
  disableRadioButtons: boolean = false;
  disableNextButton: boolean = true;
  questionNumber: number = 0;
  correctAnswers: number = 0;

  constructor(private triviaService: TriviaService) { }

  ngOnInit(): void {
    this.getTrivia();
  }

  getTrivia() {
    this.triviaService.getTrivia().subscribe({
        next: (data) => {
          this.triviaData = data;
          this.getNextQuestion();
        },
        error: (error) => {
          console.log(error);
        }
      }
    )
  }

  getNextQuestion() {
    if (this.triviaData.length) {
      const index = Math.floor(Math.random() * this.triviaData.length);
      this.question = this.triviaData[index];
      this.triviaData.splice(index, 1);
    } else {
      this.question = null;
    }

    if (this.answer) {
      this.triviaService.sendAnswer(this.answer.is_correct)
        .pipe(first())
      .subscribe({
        next: () => {},
        error: () => {}
      });
      this.questionNumber++;
      if (this.answer.is_correct) {
        this.correctAnswers++;
      }
    }

    this.answer = null;
    this.disableRadioButtons = false;
    this.disableNextButton = true;
  }

  answerSelected(event: MatRadioChange) {
    this.disableRadioButtons = true;
    this.disableNextButton = false;
  }

  getCorrectAnswer() {
    if (this.question) {
      return this.question.answers.filter(answer => answer.is_correct)[0].answer
    }
    return '';
  }

}
