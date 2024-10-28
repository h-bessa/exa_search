import React from 'react';
import { Card, Form, Input, Button, Row, Col } from 'antd';

const Login: React.FC = () => {
  const onFinish = (values: any) => {
    console.log('Success:', values);
  };

  const onFinishFailed = (errorInfo: any) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <Row justify="center" align="middle" style={{ minHeight: '100vh' }}>
      <Col>
        <Card title="Connexion" style={{ width: 300 }}>
          <Form
            layout="vertical"
            name="basic"
            initialValues={{ remember: true }}
            onFinish={onFinish}
            onFinishFailed={onFinishFailed}
          >
            <Form.Item
              label="Nom d'utilisateur"
              name="username"
              rules={[{ required: true, message: 'Veuillez entrer votre nom d\'utilisateur!' }]}
            >
              <Input />
            </Form.Item>

            <Form.Item
              label="Mot de passe"
              name="password"
              rules={[{ required: true, message: 'Veuillez entrer votre mot de passe!' }]}
            >
              <Input.Password />
            </Form.Item>

            <Form.Item style={{display: 'flex', justifyContent:'center'}}>
              <Button type="primary" htmlType="submit">
                Se connecter
              </Button>
            </Form.Item>
          </Form>
          <Button type="link" block>
            Continuer sans se connecter
          </Button>
        </Card>
      </Col>
    </Row>
  );
};

export default Login;
