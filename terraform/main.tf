provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "fastapi_server" {
  ami           = "ami-0c55b159cbfafe1f0"  # Amazon Linux 2 (atualizar se necessário)
  instance_type = "t2.micro"

  tags = {
    Name = "fastapi-instance"
  }

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y python3 git
              pip3 install fastapi uvicorn sqlalchemy python-dotenv
              git clone https://github.com/usuario/repositorio.git /home/ec2-user/app
              cd /home/ec2-user/app
              uvicorn app.main:app --host 0.0.0.0 --port 80 &
              EOF
}
