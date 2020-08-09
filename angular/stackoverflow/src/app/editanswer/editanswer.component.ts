import { Component, OnInit } from '@angular/core';
import { QuestionsService } from '../questions.service';
import { Answer, Question } from '../question';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-editanswer',
  templateUrl: './editanswer.component.html',
  styleUrls: ['./editanswer.component.css']
})
export class EditanswerComponent implements OnInit {

  constructor(
    private questionService : QuestionsService,
    private route: ActivatedRoute,
    private location: Location,
  ) { }

  ngOnInit() {
    
  }

  goBack(): void{
    this.location.back();
  }

answer_arr : Question[];

editAnswer(answer_arr) {
  console.log("abc");
  const id = +this.route.snapshot.paramMap.get('id');
  console.log(id);
  this.questionService.EditAnswer(answer_arr,id).subscribe(res => this.answer_arr = res);
}
}
