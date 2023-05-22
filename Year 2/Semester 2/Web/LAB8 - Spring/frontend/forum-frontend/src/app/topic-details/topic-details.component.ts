import {Component, OnInit, ViewChild} from '@angular/core';
import {ActivatedRoute, Router} from "@angular/router";
import {AddTopicDTO, Topic, TopicWithCommentsDTO} from "../Model/Topic";
import {TopicsService} from "../topics.service";
import {CommentsService} from "../comments.service";
import {AuthService} from "../auth.service";
import {MatPaginator} from "@angular/material/paginator";
import {MatSort} from "@angular/material/sort";
import {MatTableDataSource} from "@angular/material/table";
import {Comment, CommentUpdateDTO} from "../Model/Comment";
import {Observable} from "rxjs";
import {CoreService} from "../core.service";
import {MatDialog} from "@angular/material/dialog";
import {ConfirmationDialogComponent} from "../confirmation-dialog/confirmation-dialog.component";

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
  commentUpdate: CommentUpdateDTO = {
    content: '',
    created_by: '',
  }
  contentUpdate: string = '';

  errorMessage = "";


  @ViewChild(MatPaginator) paginator!: MatPaginator;
  @ViewChild(MatSort) sort!: MatSort;

  constructor(private route: ActivatedRoute,
              private topicSrv: TopicsService,
              private commentSrv: CommentsService,
              private AuthSrv: AuthService,
              private router: Router,
              private coreSrv: CoreService,
              private dialog: MatDialog) { }

  ngOnInit() {
    const topicId = this.route.snapshot.paramMap.get('id');
    this.topicId = topicId;
    console.log(topicId);
    this.getCommentsList();
  }

  getCommentsList(){
    this.commentSrv.getCommentsForATopic(this.topicId).subscribe({
      next: (res) => {
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

  onCommentContentChange(event: any){
    this.contentUpdate = event.target.value;
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

  CommentDetails(id: string): void {


    this.commentSrv.getAComment(id, this.topicId).subscribe(
      (res) => {

        if (res['user']['username'] === this.AuthSrv.getUsername()) {
          this.commentUpdate.content = this.contentUpdate;
          this.commentUpdate.created_by = <string>this.AuthSrv.getUsername();
          this.commentSrv.updateComment(this.commentUpdate, res['topic']['topicId'], id).subscribe(
            (response) => {
              this.coreSrv.openSnackBar('Comment detail updated!', 'done');
              this.getCommentsList();
            },
            (error) => {
              this.errorMessage = error.error.message;
              this.coreSrv.openSnackBar(this.errorMessage, 'done');
            }
          );
        }
        else{
          this.coreSrv.openSnackBar("You cant update a comment that is not yours!", 'done');
        }
      },
      (error) => {
        console.error('Error retrieving comment:', error);
      }
    );
  }

  DeleteComment(id: string): void {
    const dialogRef = this.dialog.open(ConfirmationDialogComponent, {
      data: 'Are you sure you want to delete this document?',
    });
    let yes = 0;
    dialogRef.afterClosed().subscribe((result) => {
      if (result) {
        this.commentSrv.getAComment(id, this.topicId).subscribe(
          (res) => {
            if (res['user']['username'] === this.AuthSrv.getUsername()) {
              this.commentSrv.deleteComment(res['topic']['topicId'], id).subscribe(
                (response) => {
                  this.coreSrv.openSnackBar('Comment deleted!', 'done');
                  this.getCommentsList();
                },
                (error) => {
                  this.errorMessage = error.error.message;
                  this.coreSrv.openSnackBar(this.errorMessage, 'done');
                }
              );
            } else {
              this.coreSrv.openSnackBar("You cant delete a comment that is not yours!", 'done');
            }
          },
          (error) => {
            console.error('Error retrieving comment:', error);
          }
        );
      }
    });

    }


}
