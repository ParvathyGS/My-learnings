import { Component, OnInit } from '@angular/core';
import { Post } from '../post';
import { Posts } from '../mock-post';

@Component({
  selector: 'app-posts',
  templateUrl: './posts.component.html',
  styleUrls: ['./posts.component.css']
})
export class PostsComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    console.log("haii abcd")
  }

  posts:Post[] = Posts;

  selectedPost: Post;

  onSelect(post:Post){
    this.selectedPost = post;
  }
}