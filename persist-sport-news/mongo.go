package main

import (
	"context"
	"encoding/json"
	"log"
	"net/http"

	"go.mongodb.org/mongo-driver/bson"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
)

type Server struct {
	client *mongo.Client
}

func NewServer(c *mongo.Client) *Server {
	return &Server{
		client: c,
	}
}

func (s *Server) handleGetAllGames(w http.ResponseWriter, r *http.Request) {
	coll := s.client.Database("sportnews").Collection("games")

	query := bson.M{}
	cursor, err := coll.Find(context.TODO(), query)
	if err != nil {
		log.Fatal(err)
	}

	results := []bson.M{}
	if err = cursor.All(context.TODO(), &results); err != nil {
		log.Fatal(err)
	}

	w.WriteHeader(http.StatusOK)
	w.Header().Add("Content-Type", "application/json")
	json.NewEncoder(w).Encode(results)
}

func main() {
	client, err := mongo.Connect(context.TODO(), options.Client().ApplyURI("mongodb://localhost:27017"))
	if err != nil {
		panic(err)
	}

	server := NewServer(client)
	http.HandleFunc("/games", server.handleGetAllGames)
	http.ListenAndServe(":3000", nil)
}
