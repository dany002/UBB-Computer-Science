import { Injectable } from '@angular/core';
import { HttpClient,HttpParams } from '@angular/common/http';
import {AddDocumentDto, Document} from './Document';
import {Observable} from "rxjs";
@Injectable({
  providedIn: 'root'
})
export class DocumentsService {

  constructor( private http: HttpClient) { }

  baseUrl: string = 'http://127.0.0.1:8000/';

  getDocuments() : Observable<any>{
    return this.http.get(this.baseUrl+'view.php') as Observable<any>;
  }

  getSingleDocument(id:number): Observable<Document> {
    return this.http.get(this.baseUrl+'view.php?id='+id) as Observable<Document>;
  }

  deleteDocument(id: string): Observable<any> {
    return this.http.delete(this.baseUrl+'delete.php?id='+ id) as Observable<any>;
  }

  createDocument(document:AddDocumentDto): Observable<any> {
    return this.http.post(this.baseUrl+'insert.php', document) as Observable<any>;
  }

  editDocument(documentId: number, document:Document): Observable<Document> {
    return this.http.put(this.baseUrl+`update.php?id=${documentId}`, document) as Observable<Document>; // no id for document ?
  }
}
