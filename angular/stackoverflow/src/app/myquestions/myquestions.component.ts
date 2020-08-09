import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { QuestionsService } from '../questions.service';
import { Question_details,Questions } from '../question';


@Component({
  selector: 'app-myquestions',
  templateUrl: './myquestions.component.html',
  styleUrls: ['./myquestions.component.css']
})
export class MyquestionsComponent implements OnInit {

  constructor(
    private questionService:QuestionsService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit() {
    this.Myquestion();
  }

myquestion_arr : Questions[];

Myquestion(){
  this.questionService.MyQuestion().subscribe((res) => this.myquestion_arr = res.questions);
}
}
