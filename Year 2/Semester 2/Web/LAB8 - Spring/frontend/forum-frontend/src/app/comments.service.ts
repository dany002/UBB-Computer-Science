import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Topic} from "./Model/Topic";

@Injectable({
  providedIn: 'root'
})
export class CommentsService {
  constructor(private http: HttpClient) { }

  baseUrl: string = 'http://127.0.0.1:8080/api/topics';

  getAComment(commentId: string, topicId: string | null): Observable<any>{
    return this.http.get(this.baseUrl + "/" + topicId + "/comments/" + commentId) as Observable<any>;
  }

  getCommentsForATopic(topicId: string | null): Observable<any>{
    return this.http.get(this.baseUrl + '/' + topicId + "/comments") as Observable<any>;
  }

  deleteComment(commentId: string): Observable<any>{
    return this.http.delete(this.baseUrl + "/" + commentId) as Observable<any>;
  }

  createComment(comment: { content: string; created_by: string | null }, topicId: string | null): Observable<any>{
    return this.http.post(this.baseUrl + "/" + topicId + "/comments",comment) as Observable<any>;
  }

  updateComment(commentId: string, comment:Comment): Observable<any>{
    return this.http.put(this.baseUrl,comment) as Observable<any>;
  }

}
