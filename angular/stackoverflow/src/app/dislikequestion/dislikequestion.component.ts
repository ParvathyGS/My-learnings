import { Component, OnInit } from '@angular/core';
import { QuestionsService } from '../questions.service';
import { Answer, Question } from '../question';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-dislikequestion',
  templateUrl: './dislikequestion.component.html',
  styleUrls: ['./dislikequestion.component.css']
})
export class DislikequestionComponent implements OnInit {

  constructor(
    private questionService : QuestionsService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit() {
  }

  dislikeCount : number = 0;

  dislikeQuestion() {
  
    const id = +this.route.snapshot.paramMap.get('id');
    this.dislikeCount++;
    console.log("abc");
    console.log(id);
    this.questionService.DislikeQuestion(this.dislikeCount,id).subscribe(res => this.dislikeCount = res);
   
  }
}
