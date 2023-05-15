#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 08:29:04 2023

@author: oskarjohansson
"""

import json



def login():
    while True:
        print("Welcome. Do you want to log in, create a new user or delete an existing user?")
        
        user_input = input("Enter choice \"Log in, new user or delete user\": ")
        if user_input.lower() == "new user":
            new_user_name = input("Please enter a user name: ") 
            user_list = load_user_list()
            if new_user_name in user_list:
                print("User already exist.")
            else:
                new_user = register_user(new_user_name)
                new_user = {"User name" : new_user.user_name, "User password" : new_user.user_password, "User email" : new_user.user_email, "User nationality" : new_user.user_nationality, "User id" : new_user.user_id}
                save_user(new_user)
                print('\nNew user suceccfully created!\n')
                input('Press [Enter] to continue')
                

        elif user_input.lower() == "log in":
            print("Enter user name and password.")
            user_name = input("User name: ")
            user_password = input("Enter password: ")
            user_list = load_user_list()
            for i in user_list:
                if i["User name"] == user_name and i["User password"] == user_password:
                    print('\nLogin successful!\n')
                    print("Welcome", user_name)
                    user_id = show_user_id(user_name, user_list)
                    main(user_id)
                else:
                    print("Wrong username or password")
                    input('Press [Enter] to continue')
                    break
                    
                    ## BUILD A DELETE USER FUNCTION ##
                            ##NOT FINNISHED##
        elif user_input.lower() == "delete user":
            print("Enter user name and password to delete user: ")
            user_name = input("User name: ")
            user_password = input("Enter password: ")
            user_list = load_user_list()
            for i in user_list:
                if i["User name"] == user_name and i["User password"] == user_password:
                    user = i["User name"]
                    ##FIND OUT HOW TO DELETE OBJECT FROM LIST/DICT##
                    user_input = input("Confirm delete user, Y/N: ")
                    if user_input.lower() == "y":
                        delete_user()
                        break
                    else:
                        print("returning to main menu...")
                        break

        else:
            print("Unknown command")
    
              
        ### A Class for new users ###

def main(user_id):
    user_id = user_id
    while True:
        print("Welcome. Do you want to read or write a review?")
        user_input = input("> ")
        if user_input.lower() == "write":
            new_book = write_review(user_id)
            new_book = {"author" : new_book.author , "titel" : new_book.titel, "langugage" : new_book.language, "rate" : new_book.rate, "review" : new_book.review,"user id" : user_id, "review id" : new_book.review_id}
            add_to_bookshelf(new_book)
            
        elif user_input.lower() == "read":
            read_review()
            input('Press [Enter] to continue')
        else:
            print("Unknown command")      

class User_information:
    
    def __init__(self, user_name, user_password, user_email, user_nationality, user_id = None):
        self.user_name = user_name
        self.user_password = user_password
        self.user_email = user_email
        self.user_nationality = user_nationality
        self.user_id = user_id
        if user_id is None:
            self.user_id = User_information.generate_user_id()
        else: 
            self.user_id = user_id
    
    def generate_user_id():
        user_list = load_user_list()
        user_id = len(user_list) + 1
        return user_id        

        ### Class for new reviews

class Review:
    
    def __init__(self, author, titel, language, rate, review, user_id, review_id = None):
        self.author = author
        self.titel = titel
        self.rate = rate
        self.language = language
        self.review = review
        self.user_id = user_id
        self.review_id = review_id
        if review_id is None:
            self.review_id = Review.generate_review_id()
        else: 
            self.review_id = review_id
    
    def generate_review_id():
        bookshelf = open_bookshelf()
        review_id = len(bookshelf) + 1
        return review_id

        ### Functions to open, read and write to json-files ###

def load_user_list():
    with open("user_list.json", "r") as user_list_json:
        user_list = json.load(user_list_json)
        user_list_json.close()
        return user_list
    
def save_user(new_user):
    with open ("user_list.json", "r+",) as user_list_json:
        user_list = json.load(user_list_json)
        user_list_json.seek(0)
        user_list.append(new_user)
        json.dump(user_list, user_list_json, indent=2)
        user_list_json.close()
        
def delete_user(user_list):
    with open ("user_list.json", "w",) as user_list_json:
        json.dump(user_list, user_list_json)
        user_list_json.close()

def show_user_id(name, user_list):
    for i in user_list:
        if i["User name"] == name:
            return(i["User id"])

def open_bookshelf():
    with open("bookshelf.json", "r") as bookshelf_json:
        bookshelf = json.load(bookshelf_json)
        bookshelf_json.close()
        return bookshelf   

            # A function to add books to the bookshelf in json format.
            
def add_to_bookshelf(new_book):
    with open ("bookshelf.json", "r+",) as bookshelf_json:
        bookshelf = json.load(bookshelf_json)
        bookshelf_json.seek(0)
        bookshelf.append(new_book)
        json.dump(bookshelf, bookshelf_json, indent=2)
        bookshelf_json.truncate()
        bookshelf_json.close()
        
def register_user(user_input):
    name = user_input
    password = input("Enter your password: ")
    email = input("Enter your e-mail adress: ")
    nationality = input("Enter your nationality: ")
    new_user = User_information(name, password, email, nationality)
    return new_user        
        
        ### ^^^^ Functions to open, read and write to json-files ^^^^ ### 

def write_review(user_id):
    author = input("Enter author name: ")
    titel = input("Enter titel: ")
    language = input("Enter language: ")
    rate = input("Add rate: ")
    review = input("Enter Review. Maximum of 256 characters: ")
    while True:
        if len(review) > 256:
            print("To many characters. Maximum is 256.")     
        else:
            new_book = Review(author, titel, language, rate, review, user_id)
            #ADD FUNCTION TO ADD REVIEW TO THE USER_ID
            return new_book
            #ADD FUNCTION TO LET THE USER INSERT ISBN TO GET INFORMATION ABOUT THE BOOK VIA API. 
            #SUPERFEATURE, ADD FUNCTION TO READ ISBN WITH CAMERA.


def delete_review(review_id):
    bookshelf = open_bookshelf()

def read_review():
    bookshelf = open_bookshelf()
    user_input = input("Enter author name: ")
    result = []
    for i,review in enumerate(bookshelf):
        for k,v in review.items():
            if user_input == v:
                result.append(bookshelf[i])
    if len(result) < 1:
        print("No Results")
    else:
        print(result)


        #for k in i:
        #   print(k == user_input)
        #    if user_input == k:
        #        print(bookshelf[i])
        #        break
     
      
        #if k == user_input:
        #    print(bookshelf[i])
        #else:
        #    print("No match found")


#connection = create_connection("E:\\sm_app.sqlite") #The following script creates a connection to the SQLite database:

user_list = load_user_list()

login()
