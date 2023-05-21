import {Component, OnInit, ViewChild} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {AddTopicDTO, Topic, TopicWithCommentsDTO} from "../Model/Topic";
import {TopicsService} from "../topics.service";
import {CommentsService} from "../comments.service";
import {AuthService} from "../auth.service";
import {MatPaginator} from "@angular/material/paginator";
import {MatSort} from "@angular/material/sort";
import {MatTableDataSource} from "@angular/material/table";
import {Comment} from "../Model/Comment";
import {Observable} from "rxjs";

@Component({
  selector: 'app-topic-details',
  templateUrl: './topic-details.component.html',
  styleUrls: ['./topic-details.component.css']
})
export class TopicDetailsComponent implements OnInit{
  topic: TopicWithCommentsDTO | undefined;
  newComment: string = '';
  displayedColumns: string[] = ['id', 'content', 'created_by', 'action'];
  topicId: string | null = '';
  dataSource!: MatTableDataSource<Comment>;


  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;
  private comment: Comment;
  constructor(private route: ActivatedRoute,
              private topicSrv: TopicsService,
              private commentSrv: CommentsService,
              private AuthSrv: AuthService,
              private router: Router) { }

  ngOnInit() {
    const topicId = this.route.snapshot.paramMap.get('id');
    this.topicId = topicId;
    console.log(topicId);
    this.getCommentsList();
  }

  getCommentsList(){
    this.commentSrv.getCommentsForATopic(this.topicId).subscribe({
      next: (res) => {
        console.log("Comment!");
        console.log(res[0]);
        this.dataSource = new MatTableDataSource(res);
        this.dataSource.sort = this.sort;
        this.dataSource.paginator = this.paginator;
      },
      error: (err) => {
        console.log(err);
      }
    });
  }


  onCommentNameChange(event: any) {
    this.newComment = event.target.value;
  }


  addComment(): void {
    console.log(this.newComment);
    if (this.newComment.trim() !== '') {
      const newCom = {content: this.newComment, created_by: this.AuthSrv.getUsername()}; // Modify to include the 'created_by' field
      console.log("NEW COM: " + newCom)
      this.commentSrv.createComment(newCom, this.topicId).subscribe(
        (response) => {
          console.log('Comment added successfully:', response);
          this.newComment = '';
          this.getCommentsList();
        },
        (error) => {
          // Handle error
          console.error('Error adding comment:', error);
        }
      );
    }
  }

  CommentDetails(id: string): void{ //TODO !!!
    console.log(id);
    const comment_for_update = this.commentSrv.getAComment(id, this.topicId);
    this.commentSrv.getAComment(id, this.topicId).subscribe({
      next: (res) => {
        console.log(res['user']['username']);
        console.log(this.AuthSrv.getUsername());
        if(res['user']['username'] == this.AuthSrv.getUsername()){
          const help_comment: string = "ASD";
          this.comment.content = help_comment;
          this.comment.created_by = this.AuthSrv.getUsername();
          this.commentSrv.updateComment(id, comment);
        }
      }
    //this.router.navigate(['/comment-details/',id]);
    })
  }
}
