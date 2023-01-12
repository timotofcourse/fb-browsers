import time
import PySide6
import subprocess
from tkinter import messagebox


def pre():
    policy = 'Set-ExecutionPolicy RemoteSigned -Scope CurrentUser'
    install = 'irm get.scoop.sh | iex'
    definepolicy = subprocess.Popen(policy, shell=True)
    definepolicy.wait()
    runinstall = subprocess.Popen(install, shell=True)
    runinstall.wait()

def git():
    gitinstall = 'scoop install git'
    rungitinstall = subprocess.Popen(gitinstall, shell=True)
    rungitinstall.wait()

buckets = ['main', 'extras', 'java', 'nonportable', 'games', 'filmabem' ]
officialbuckets = [buckets[0], buckets[1], buckets[2], buckets[3], buckets[4]]
fbbucket = buckets[-1]
bucketcmd = 'scoop bucket add '
custombucket = ' https://github.com/FilmaBem2/applications.git'
mainbucket = bucketcmd + buckets[0]
extrasbucket = bucketcmd + buckets[1]
javabucket = bucketcmd + buckets[2]
npbucket = bucketcmd + buckets[3]
gamesbucket = bucketcmd + buckets[4]
fbbucket = bucketcmd + buckets[-1] + custombucket

def bucketadd():
    add1bucket = subprocess.Popen(mainbucket, shell=True)
    add1bucket.wait()
    add2bucket = subprocess.Popen(extrasbucket, shell=True)
    add2bucket.wait()
    add3bucket = subprocess.Popen(javabucket, shell=True)
    add3bucket.wait()
    add4bucket = subprocess.Popen(npbucket, shell=True)
    add4bucket.wait()
    add5bucket = subprocess.Popen(gamesbucket, shell=True)
    add5bucket.wait()
    addfbbucket = subprocess.Popen(fbbucket, shell=True)
    addfbbucket.wait()