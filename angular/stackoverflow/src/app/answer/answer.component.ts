import { Component, OnInit } from '@angular/core';
import { QuestionsService } from '../questions.service';
import { Answer, Question } from '../question';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-answer',
  templateUrl: './answer.component.html',
  styleUrls: ['./answer.component.css']
})
export class AnswerComponent implements OnInit {

  constructor(
    private questionService : QuestionsService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit() {
  }

  answer_arr : Question[];

  addAnswer(answer_arr){
    const id = +this.route.snapshot.paramMap.get('id');
    this.questionService.AddAnswer(answer_arr,id).subscribe(res => console.log(res));
  }
}
