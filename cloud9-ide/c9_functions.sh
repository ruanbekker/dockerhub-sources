c9(){
  localip="localhost"
  name="${1:-c9}"
  workspace="${2:-$(pwd)}"
  username="${3:-admin}"
  password="${4:-admin}"

  if [ "$1" == "help" ]
    then
      echo "c9 name-of-container /path/to/workspace myuser mypass"
  fi

  docker run --rm --name ${name} -d -P -e USERNAME=${username} -e PASSWORD=${password} -v "$workspace:/workspace" ruanbekker/cloud9-ide
  port="$(docker inspect --format '{{ range $key, $value := .NetworkSettings.Ports }}{{ if eq $key "8000/tcp" }}{{ (index $value 0).HostPort }}{{ end }}{{ end }}' ${name})"

  echo -n "Cloud9 IDE Available at:\n"
  echo
  echo "Instance Name: ${name}"
  echo "Workspace: ${workspace}"
  echo "Port: ${port}"
  echo "Username: ${username}"
  echo "Password: ${password}"
  echo "Local : http://${localip}:${port}"
  echo
}

c9_list(){
  docker inspect --format '{{.Name}}' $(docker ps -q) | cut -d '/' -f2
}

c9_kill(){
  docker rm -f ${name}
}
