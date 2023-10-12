export interface Document{
  id: number;
  author: string;
  title: string;
  pages: number;
  types: string;
  format: string;
}

export interface AddDocumentDto{
  author: string;
  title: string;
  pages: number;
  types: string;
  format: string;
}