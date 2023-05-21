import { Injectable } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {SignUpDTO} from "./Model/SignUpDTO";
import {Observable} from "rxjs";
import {LogInDTO} from "./Model/LogInDTO";
import {AddTopicDTO, Topic} from "./Model/Topic";

@Injectable({
  providedIn: 'root'
})
export class TopicsService {

  constructor(private http: HttpClient) { }

  baseUrl: string = 'http://127.0.0.1:8080/api/topics';

  getTopics(): Observable<any>{
    return this.http.get(this.baseUrl) as Observable<any>;
  }

  getTopic(topicId: string) : Observable<any>{
    return this.http.get(this.baseUrl + "/" + topicId) as Observable<any>;
  }

  deleteTopic(topicId: string): Observable<any>{
    return this.http.delete(this.baseUrl + "/" + topicId) as Observable<any>;
  }

  createTopic(topic: { name: string; created_by: string | null }): Observable<any>{
    return this.http.post(this.baseUrl,topic) as Observable<any>;
  }

  updateTopic(topicId: string, topic:Topic): Observable<any>{
    return this.http.put(this.baseUrl,topic) as Observable<any>;
  }

}
