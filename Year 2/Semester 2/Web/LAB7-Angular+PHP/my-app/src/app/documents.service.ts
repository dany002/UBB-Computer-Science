import { Injectable } from '@angular/core';
import { HttpClient,HttpParams } from '@angular/common/http';
import { Document } from './Document';
@Injectable({
  providedIn: 'root'
})
export class DocumentsService {

  constructor( private http: HttpClient) { }
  baseUrl: string = 'http://localhost:8000/';

  getDocuments() {
    return this.http.get<Document[]>(this.baseUrl+'view.php');
  }

  getSingleDocument(id:any) {
    return this.http.get<Document[]>(this.baseUrl+'view.php?id='+id);
  }

  deleteDocument(id:any) {
    console.log(id);
    return this.http.delete(this.baseUrl+'delete.php?id='+ id);
  }

  createDocument(document:any) {
    return this.http.post(this.baseUrl+'insert.php', document);
  }

  editDocument(document:any) {
    return this.http.put(this.baseUrl+'update.php', document);
  }
}
