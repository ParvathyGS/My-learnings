import { Component, OnInit } from '@angular/core';
import { ActivatedRoute,Router } from '@angular/router';
import { Location } from '@angular/common';
import { User } from '../user';
import { UserService } from '../user.service';
import { MessageService } from '../message.service';
import { QuestionsService } from '../questions.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent implements OnInit {

  constructor(
    private route:ActivatedRoute,
    private location:Location,
    private userService: UserService,
    private router: Router,
    private messageService: MessageService,
    private questionService : QuestionsService,
  ) { }

  ngOnInit() {
  }

  // data: Object = {};
  // user1  : User;
  onSubmit(user_details:any) {
    console.log(user_details);
    this.messageService.add('Login Successful');
    this.userService.loginAction(user_details).subscribe(
      res => 
        {
          localStorage.setItem("userToken",res.token);
          var userId: any = res.user.id;
          localStorage.setItem("userId",userId);

          // console.log("userriddd");
          // console.log(localStorage.getItem("userId"));

          // console.log("userToken");
          // console.log(localStorage.getItem("userToken"));
         
          if(this.questionService.isLoggedIn()) {
            this.router.navigateByUrl("/ask-questions");
          }else{
            this.router.navigateByUrl("/login");
          }
        }
    );
  }
}
