import { Component, OnInit } from '@angular/core';
import { DocumentsService } from '../documents.service';

@Component({
  selector: 'app-list-documents',
  templateUrl: './list-documents.component.html',
  styleUrls: ['./list-documents.component.sass']
})
export class ListDocumentsComponent implements OnInit{
  documents: any;

  constructor( private documentservice: DocumentsService) { }

  ngOnInit(): void {

    this.documentservice.getDocuments().subscribe(
      (result:any)=>{
        //console.log(result)
        this.documents = result.data;
      }
    )

  }

  deleteDocument(document:any){
    // console.log(id);
    this.documentservice.deleteDocument(document.id).subscribe(data=>{
      this.documents = this.documents.filter((u: any) => u !== document);
    })
  }

}
