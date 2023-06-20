import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Observable} from "rxjs";
import {AddDocumentDto} from "./Model/Document";

@Injectable({
  providedIn: 'root'
})
export class DocumentService {

  constructor( private http: HttpClient) { }

  baseUrl: string = 'http://127.0.0.1:5000/Documents/';

  httpOptions = {
    headers: new HttpHeaders({
      'Content-Type':  'application/json',
      'Authorization': 'Bearer ' + localStorage.getItem('token')
    })
  };

  getDocuments() : Observable<any>{
    return this.http.get(this.baseUrl, this.httpOptions) as Observable<any>;
  }

  getSingleDocument(id:number): Observable<Document> {
    return this.http.get(this.baseUrl + id, this.httpOptions) as Observable<Document>;
  }

  deleteDocument(id: string): Observable<any> {
    return this.http.delete(this.baseUrl + id, this.httpOptions) as Observable<any>;
  }

  createDocument(document:AddDocumentDto): Observable<any> {
    return this.http.post(this.baseUrl, document, this.httpOptions) as Observable<any>;
  }

  editDocument(documentId: number, document:Document): Observable<Document> {
    return this.http.put(this.baseUrl + documentId, document, this.httpOptions) as Observable<Document>;
  }
}
