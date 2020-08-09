import { Component, OnInit } from '@angular/core';
import { QuestionsService } from '../questions.service';
import { Answer, Question } from '../question';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-answersbyme',
  templateUrl: './answersbyme.component.html',
  styleUrls: ['./answersbyme.component.css']
})
export class AnswersbymeComponent implements OnInit {

  constructor(
    private questionService : QuestionsService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit()  { 
    this.Myanswers();
   }

my_ans : Question[];

Myanswers(){
  console.log("abc");
  this.questionService.MyAnswers().subscribe(res => console.log(res));//(res) => this.my_ans = res);
}
}
