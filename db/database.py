# -*- coding: utf-8 -*-
import os
import sqlite3
from sys import argv

class DbGolfManager(object):
	def __init__(self):
		self.DATABASE = "db_golf_manager.sqlite"

	def execute_scripts_from_file(self, filename):
		# Open and read the file as a single buffer
		fd = open(filename, 'r')
		sqlFile = fd.read()
		fd.close()

		# all SQL commands (split on ';')
		sqlCommands = sqlFile.split(';')
		conn = sqlite3.connect(self.DATABASE)
		cur = conn.cursor()
		# Execute every command from the input file
		for command in sqlCommands:
			# This will skip and report errors
			# For example, if the tables do not yet exist, this will skip over
			# the DROP TABLE commands
			try:
				cur.execute(command)
			except sqlite3.OperationalError as e:
				print("Command skipped: ", e.args)
			print("Databse create")

	def insert_into(self, table, data):
		"""Attention data doit être une liste de tuples ! 
		"""
		try:
			# connexion à la base sqlite3
			conn = sqlite3.connect(self.DATABASE)
			cur = conn.cursor()
			# insertion des données
			cur.executemany("INSERT INTO " + table + "(" + self.CONST.construct_querry_attributes(
				table) + ") VALUES (" + self.CONST.string_interrogation(table) + ")", data)

			conn.commit()
			# fin de la requête
			cur.close()
			conn.close()
			print("insertion réussie")
		except sqlite3.IntegrityError:
			print("echec insertion : violation clef primaire")

	def execute_sql(self, requete_sql):
		# connexion à la base sqlite3
		conn = sqlite3.connect(self.DATABASE)
		cur = conn.cursor()
		# querry
		try:
			cur.execute(requete_sql)
			res = cur.fetchall()

			# recuperation de l'entete
			info = cur.description

			# fin de la requête
			cur.close()
			conn.close()
			entete = list()
			# constitution de l'entete
			for elem in info:
				if elem != None:
					# récuperation du nom de la colonne
					entete.append(elem[0])

		# cas ou l'on s'est planté dans la requête
		except sqlite3.OperationalError as e:
			entete = ""
			res = str(e.args)

		return entete, res

# Main du programme
if __name__ == "__main__":
	
	db = DbGolfManager()
	db.execute_scripts_from_file("./create_db.sql")

