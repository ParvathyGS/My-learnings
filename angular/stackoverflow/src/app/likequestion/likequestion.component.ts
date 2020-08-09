import { Component, OnInit } from '@angular/core';
import { QuestionsService } from '../questions.service';
import { Answer, Question } from '../question';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-likequestion',
  templateUrl: './likequestion.component.html',
  styleUrls: ['./likequestion.component.css']
})
export class LikequestionComponent implements OnInit {

  constructor(
    private questionService : QuestionsService,
    private route: ActivatedRoute,
  ) { }

  ngOnInit() {
    this.likeQuestion();
  }

likeCount : number = 0;
dislikeCount : number = 0;
question : Question;

likeQuestion() {
  
  const id = +this.route.snapshot.paramMap.get('id');
  this.likeCount++;
  console.log("abc");
  console.log(id);
  this.questionService.LikeQuestion(this.likeCount,id).subscribe(res => this.likeCount = res);
 
}
}
