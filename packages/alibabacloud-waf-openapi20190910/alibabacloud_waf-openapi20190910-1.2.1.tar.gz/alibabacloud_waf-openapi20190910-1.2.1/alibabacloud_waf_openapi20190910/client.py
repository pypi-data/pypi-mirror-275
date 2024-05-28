# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_waf_openapi20190910 import models as waf_openapi_20190910_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-chengdu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-zhangjiakou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-huhehaote': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hangzhou': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-heyuan': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-wulanchabu': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-west-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'eu-central-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'wafopenapi.ap-southeast-1.aliyuncs.com',
            'cn-shanghai-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'wafopenapi.cn-hangzhou.aliyuncs.com',
            'cn-north-2-gov-1': 'wafopenapi.cn-hangzhou.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('waf-openapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_certificate_with_options(
        self,
        request: waf_openapi_20190910_models.CreateCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateCertificateResponse:
        """
        @param request: CreateCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certificate_with_options_async(
        self,
        request: waf_openapi_20190910_models.CreateCertificateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateCertificateResponse:
        """
        @param request: CreateCertificateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.certificate_name):
            query['CertificateName'] = request.certificate_name
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateCertificateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certificate(
        self,
        request: waf_openapi_20190910_models.CreateCertificateRequest,
    ) -> waf_openapi_20190910_models.CreateCertificateResponse:
        """
        @param request: CreateCertificateRequest
        @return: CreateCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_with_options(request, runtime)

    async def create_certificate_async(
        self,
        request: waf_openapi_20190910_models.CreateCertificateRequest,
    ) -> waf_openapi_20190910_models.CreateCertificateResponse:
        """
        @param request: CreateCertificateRequest
        @return: CreateCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_with_options_async(request, runtime)

    def create_certificate_by_certificate_id_with_options(
        self,
        request: waf_openapi_20190910_models.CreateCertificateByCertificateIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse:
        """
        @param request: CreateCertificateByCertificateIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateByCertificateIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificateByCertificateId',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_certificate_by_certificate_id_with_options_async(
        self,
        request: waf_openapi_20190910_models.CreateCertificateByCertificateIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse:
        """
        @param request: CreateCertificateByCertificateIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCertificateByCertificateIdResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate_id):
            query['CertificateId'] = request.certificate_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCertificateByCertificateId',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_certificate_by_certificate_id(
        self,
        request: waf_openapi_20190910_models.CreateCertificateByCertificateIdRequest,
    ) -> waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse:
        """
        @param request: CreateCertificateByCertificateIdRequest
        @return: CreateCertificateByCertificateIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_certificate_by_certificate_id_with_options(request, runtime)

    async def create_certificate_by_certificate_id_async(
        self,
        request: waf_openapi_20190910_models.CreateCertificateByCertificateIdRequest,
    ) -> waf_openapi_20190910_models.CreateCertificateByCertificateIdResponse:
        """
        @param request: CreateCertificateByCertificateIdRequest
        @return: CreateCertificateByCertificateIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_certificate_by_certificate_id_with_options_async(request, runtime)

    def create_domain_with_options(
        self,
        request: waf_openapi_20190910_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateDomainResponse:
        """
        @param request: CreateDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_header_mode):
            query['AccessHeaderMode'] = request.access_header_mode
        if not UtilClient.is_unset(request.access_headers):
            query['AccessHeaders'] = request.access_headers
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.cloud_native_instances):
            query['CloudNativeInstances'] = request.cloud_native_instances
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.connection_time):
            query['ConnectionTime'] = request.connection_time
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.http_2port):
            query['Http2Port'] = request.http_2port
        if not UtilClient.is_unset(request.http_port):
            query['HttpPort'] = request.http_port
        if not UtilClient.is_unset(request.http_to_user_ip):
            query['HttpToUserIp'] = request.http_to_user_ip
        if not UtilClient.is_unset(request.https_port):
            query['HttpsPort'] = request.https_port
        if not UtilClient.is_unset(request.https_redirect):
            query['HttpsRedirect'] = request.https_redirect
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_follow_status):
            query['IpFollowStatus'] = request.ip_follow_status
        if not UtilClient.is_unset(request.is_access_product):
            query['IsAccessProduct'] = request.is_access_product
        if not UtilClient.is_unset(request.keepalive):
            query['Keepalive'] = request.keepalive
        if not UtilClient.is_unset(request.keepalive_requests):
            query['KeepaliveRequests'] = request.keepalive_requests
        if not UtilClient.is_unset(request.keepalive_timeout):
            query['KeepaliveTimeout'] = request.keepalive_timeout
        if not UtilClient.is_unset(request.load_balancing):
            query['LoadBalancing'] = request.load_balancing
        if not UtilClient.is_unset(request.log_headers):
            query['LogHeaders'] = request.log_headers
        if not UtilClient.is_unset(request.read_time):
            query['ReadTime'] = request.read_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retry):
            query['Retry'] = request.retry
        if not UtilClient.is_unset(request.sni_host):
            query['SniHost'] = request.sni_host
        if not UtilClient.is_unset(request.sni_status):
            query['SniStatus'] = request.sni_status
        if not UtilClient.is_unset(request.source_ips):
            query['SourceIps'] = request.source_ips
        if not UtilClient.is_unset(request.write_time):
            query['WriteTime'] = request.write_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_domain_with_options_async(
        self,
        request: waf_openapi_20190910_models.CreateDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateDomainResponse:
        """
        @param request: CreateDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_header_mode):
            query['AccessHeaderMode'] = request.access_header_mode
        if not UtilClient.is_unset(request.access_headers):
            query['AccessHeaders'] = request.access_headers
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.cloud_native_instances):
            query['CloudNativeInstances'] = request.cloud_native_instances
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.connection_time):
            query['ConnectionTime'] = request.connection_time
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.http_2port):
            query['Http2Port'] = request.http_2port
        if not UtilClient.is_unset(request.http_port):
            query['HttpPort'] = request.http_port
        if not UtilClient.is_unset(request.http_to_user_ip):
            query['HttpToUserIp'] = request.http_to_user_ip
        if not UtilClient.is_unset(request.https_port):
            query['HttpsPort'] = request.https_port
        if not UtilClient.is_unset(request.https_redirect):
            query['HttpsRedirect'] = request.https_redirect
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_follow_status):
            query['IpFollowStatus'] = request.ip_follow_status
        if not UtilClient.is_unset(request.is_access_product):
            query['IsAccessProduct'] = request.is_access_product
        if not UtilClient.is_unset(request.keepalive):
            query['Keepalive'] = request.keepalive
        if not UtilClient.is_unset(request.keepalive_requests):
            query['KeepaliveRequests'] = request.keepalive_requests
        if not UtilClient.is_unset(request.keepalive_timeout):
            query['KeepaliveTimeout'] = request.keepalive_timeout
        if not UtilClient.is_unset(request.load_balancing):
            query['LoadBalancing'] = request.load_balancing
        if not UtilClient.is_unset(request.log_headers):
            query['LogHeaders'] = request.log_headers
        if not UtilClient.is_unset(request.read_time):
            query['ReadTime'] = request.read_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retry):
            query['Retry'] = request.retry
        if not UtilClient.is_unset(request.sni_host):
            query['SniHost'] = request.sni_host
        if not UtilClient.is_unset(request.sni_status):
            query['SniStatus'] = request.sni_status
        if not UtilClient.is_unset(request.source_ips):
            query['SourceIps'] = request.source_ips
        if not UtilClient.is_unset(request.write_time):
            query['WriteTime'] = request.write_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_domain(
        self,
        request: waf_openapi_20190910_models.CreateDomainRequest,
    ) -> waf_openapi_20190910_models.CreateDomainResponse:
        """
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_domain_with_options(request, runtime)

    async def create_domain_async(
        self,
        request: waf_openapi_20190910_models.CreateDomainRequest,
    ) -> waf_openapi_20190910_models.CreateDomainResponse:
        """
        @param request: CreateDomainRequest
        @return: CreateDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_domain_with_options_async(request, runtime)

    def create_protection_module_rule_with_options(
        self,
        request: waf_openapi_20190910_models.CreateProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateProtectionModuleRuleResponse:
        """
        @param request: CreateProtectionModuleRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProtectionModuleRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProtectionModuleRule',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateProtectionModuleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_protection_module_rule_with_options_async(
        self,
        request: waf_openapi_20190910_models.CreateProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.CreateProtectionModuleRuleResponse:
        """
        @param request: CreateProtectionModuleRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProtectionModuleRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProtectionModuleRule',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.CreateProtectionModuleRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_protection_module_rule(
        self,
        request: waf_openapi_20190910_models.CreateProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.CreateProtectionModuleRuleResponse:
        """
        @param request: CreateProtectionModuleRuleRequest
        @return: CreateProtectionModuleRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_protection_module_rule_with_options(request, runtime)

    async def create_protection_module_rule_async(
        self,
        request: waf_openapi_20190910_models.CreateProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.CreateProtectionModuleRuleResponse:
        """
        @param request: CreateProtectionModuleRuleRequest
        @return: CreateProtectionModuleRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_protection_module_rule_with_options_async(request, runtime)

    def delete_domain_with_options(
        self,
        request: waf_openapi_20190910_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteDomainResponse:
        """
        @param request: DeleteDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_domain_with_options_async(
        self,
        request: waf_openapi_20190910_models.DeleteDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteDomainResponse:
        """
        @param request: DeleteDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_domain(
        self,
        request: waf_openapi_20190910_models.DeleteDomainRequest,
    ) -> waf_openapi_20190910_models.DeleteDomainResponse:
        """
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_with_options(request, runtime)

    async def delete_domain_async(
        self,
        request: waf_openapi_20190910_models.DeleteDomainRequest,
    ) -> waf_openapi_20190910_models.DeleteDomainResponse:
        """
        @param request: DeleteDomainRequest
        @return: DeleteDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_domain_with_options_async(request, runtime)

    def delete_instance_with_options(
        self,
        request: waf_openapi_20190910_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_with_options_async(
        self,
        request: waf_openapi_20190910_models.DeleteInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance(
        self,
        request: waf_openapi_20190910_models.DeleteInstanceRequest,
    ) -> waf_openapi_20190910_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    async def delete_instance_async(
        self,
        request: waf_openapi_20190910_models.DeleteInstanceRequest,
    ) -> waf_openapi_20190910_models.DeleteInstanceResponse:
        """
        @param request: DeleteInstanceRequest
        @return: DeleteInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_instance_with_options_async(request, runtime)

    def delete_protection_module_rule_with_options(
        self,
        request: waf_openapi_20190910_models.DeleteProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse:
        """
        @param request: DeleteProtectionModuleRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProtectionModuleRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtectionModuleRule',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_protection_module_rule_with_options_async(
        self,
        request: waf_openapi_20190910_models.DeleteProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse:
        """
        @param request: DeleteProtectionModuleRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProtectionModuleRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProtectionModuleRule',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_protection_module_rule(
        self,
        request: waf_openapi_20190910_models.DeleteProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse:
        """
        @param request: DeleteProtectionModuleRuleRequest
        @return: DeleteProtectionModuleRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_protection_module_rule_with_options(request, runtime)

    async def delete_protection_module_rule_async(
        self,
        request: waf_openapi_20190910_models.DeleteProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.DeleteProtectionModuleRuleResponse:
        """
        @param request: DeleteProtectionModuleRuleRequest
        @return: DeleteProtectionModuleRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_protection_module_rule_with_options_async(request, runtime)

    def describe_cert_match_status_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeCertMatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeCertMatchStatusResponse:
        """
        @param request: DescribeCertMatchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertMatchStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertMatchStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeCertMatchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cert_match_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeCertMatchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeCertMatchStatusResponse:
        """
        @param request: DescribeCertMatchStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertMatchStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.certificate):
            query['Certificate'] = request.certificate
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertMatchStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeCertMatchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cert_match_status(
        self,
        request: waf_openapi_20190910_models.DescribeCertMatchStatusRequest,
    ) -> waf_openapi_20190910_models.DescribeCertMatchStatusResponse:
        """
        @param request: DescribeCertMatchStatusRequest
        @return: DescribeCertMatchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cert_match_status_with_options(request, runtime)

    async def describe_cert_match_status_async(
        self,
        request: waf_openapi_20190910_models.DescribeCertMatchStatusRequest,
    ) -> waf_openapi_20190910_models.DescribeCertMatchStatusResponse:
        """
        @param request: DescribeCertMatchStatusRequest
        @return: DescribeCertMatchStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cert_match_status_with_options_async(request, runtime)

    def describe_certificates_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeCertificatesResponse:
        """
        @param request: DescribeCertificatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertificatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificates',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_certificates_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeCertificatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeCertificatesResponse:
        """
        @param request: DescribeCertificatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeCertificatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCertificates',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeCertificatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_certificates(
        self,
        request: waf_openapi_20190910_models.DescribeCertificatesRequest,
    ) -> waf_openapi_20190910_models.DescribeCertificatesResponse:
        """
        @param request: DescribeCertificatesRequest
        @return: DescribeCertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_certificates_with_options(request, runtime)

    async def describe_certificates_async(
        self,
        request: waf_openapi_20190910_models.DescribeCertificatesRequest,
    ) -> waf_openapi_20190910_models.DescribeCertificatesResponse:
        """
        @param request: DescribeCertificatesRequest
        @return: DescribeCertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_certificates_with_options_async(request, runtime)

    def describe_domain_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainResponse:
        """
        @param request: DescribeDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainResponse:
        """
        @param request: DescribeDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainResponse:
        """
        @param request: DescribeDomainRequest
        @return: DescribeDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_options(request, runtime)

    async def describe_domain_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainResponse:
        """
        @param request: DescribeDomainRequest
        @return: DescribeDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_with_options_async(request, runtime)

    def describe_domain_advance_configs_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeDomainAdvanceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse:
        """
        @param request: DescribeDomainAdvanceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAdvanceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAdvanceConfigs',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_advance_configs_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainAdvanceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse:
        """
        @param request: DescribeDomainAdvanceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainAdvanceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_list):
            query['DomainList'] = request.domain_list
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainAdvanceConfigs',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_advance_configs(
        self,
        request: waf_openapi_20190910_models.DescribeDomainAdvanceConfigsRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse:
        """
        @param request: DescribeDomainAdvanceConfigsRequest
        @return: DescribeDomainAdvanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_advance_configs_with_options(request, runtime)

    async def describe_domain_advance_configs_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainAdvanceConfigsRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainAdvanceConfigsResponse:
        """
        @param request: DescribeDomainAdvanceConfigsRequest
        @return: DescribeDomainAdvanceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_advance_configs_with_options_async(request, runtime)

    def describe_domain_basic_configs_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeDomainBasicConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse:
        """
        @param request: DescribeDomainBasicConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainBasicConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.cloud_native_product_id):
            query['CloudNativeProductId'] = request.cloud_native_product_id
        if not UtilClient.is_unset(request.domain_key):
            query['DomainKey'] = request.domain_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainBasicConfigs',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_basic_configs_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainBasicConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse:
        """
        @param request: DescribeDomainBasicConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainBasicConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.cloud_native_product_id):
            query['CloudNativeProductId'] = request.cloud_native_product_id
        if not UtilClient.is_unset(request.domain_key):
            query['DomainKey'] = request.domain_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainBasicConfigs',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_basic_configs(
        self,
        request: waf_openapi_20190910_models.DescribeDomainBasicConfigsRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse:
        """
        @param request: DescribeDomainBasicConfigsRequest
        @return: DescribeDomainBasicConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_basic_configs_with_options(request, runtime)

    async def describe_domain_basic_configs_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainBasicConfigsRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainBasicConfigsResponse:
        """
        @param request: DescribeDomainBasicConfigsRequest
        @return: DescribeDomainBasicConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_basic_configs_with_options_async(request, runtime)

    def describe_domain_list_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainListResponse:
        """
        @param request: DescribeDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_sub):
            query['IsSub'] = request.is_sub
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainList',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_list_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainListResponse:
        """
        @param request: DescribeDomainListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_sub):
            query['IsSub'] = request.is_sub
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainList',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_list(
        self,
        request: waf_openapi_20190910_models.DescribeDomainListRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainListResponse:
        """
        @param request: DescribeDomainListRequest
        @return: DescribeDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_list_with_options(request, runtime)

    async def describe_domain_list_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainListRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainListResponse:
        """
        @param request: DescribeDomainListRequest
        @return: DescribeDomainListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_list_with_options_async(request, runtime)

    def describe_domain_names_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeDomainNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainNamesResponse:
        """
        @param request: DescribeDomainNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainNamesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainNames',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_names_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainNamesResponse:
        """
        @param request: DescribeDomainNamesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainNamesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainNames',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_names(
        self,
        request: waf_openapi_20190910_models.DescribeDomainNamesRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainNamesResponse:
        """
        @param request: DescribeDomainNamesRequest
        @return: DescribeDomainNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_names_with_options(request, runtime)

    async def describe_domain_names_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainNamesRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainNamesResponse:
        """
        @param request: DescribeDomainNamesRequest
        @return: DescribeDomainNamesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_names_with_options_async(request, runtime)

    def describe_domain_rule_group_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainRuleGroupResponse:
        """
        @param request: DescribeDomainRuleGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRuleGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRuleGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainRuleGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_domain_rule_group_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeDomainRuleGroupResponse:
        """
        @param request: DescribeDomainRuleGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDomainRuleGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainRuleGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeDomainRuleGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_domain_rule_group(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRuleGroupRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainRuleGroupResponse:
        """
        @param request: DescribeDomainRuleGroupRequest
        @return: DescribeDomainRuleGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_rule_group_with_options(request, runtime)

    async def describe_domain_rule_group_async(
        self,
        request: waf_openapi_20190910_models.DescribeDomainRuleGroupRequest,
    ) -> waf_openapi_20190910_models.DescribeDomainRuleGroupResponse:
        """
        @param request: DescribeDomainRuleGroupRequest
        @return: DescribeDomainRuleGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_domain_rule_group_with_options_async(request, runtime)

    def describe_instance_info_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfoResponse:
        """
        @description ## Usage notes
        You can call the DescribeInstanceInfo operation to query the information about the WAF instance within your Alibaba Cloud account. The information includes the ID, version, status, and expiration time of the instance.
        
        @param request: DescribeInstanceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceInfo',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeInstanceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_info_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfoResponse:
        """
        @description ## Usage notes
        You can call the DescribeInstanceInfo operation to query the information about the WAF instance within your Alibaba Cloud account. The information includes the ID, version, status, and expiration time of the instance.
        
        @param request: DescribeInstanceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceInfo',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeInstanceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_info(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfoRequest,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfoResponse:
        """
        @description ## Usage notes
        You can call the DescribeInstanceInfo operation to query the information about the WAF instance within your Alibaba Cloud account. The information includes the ID, version, status, and expiration time of the instance.
        
        @param request: DescribeInstanceInfoRequest
        @return: DescribeInstanceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_info_with_options(request, runtime)

    async def describe_instance_info_async(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceInfoRequest,
    ) -> waf_openapi_20190910_models.DescribeInstanceInfoResponse:
        """
        @description ## Usage notes
        You can call the DescribeInstanceInfo operation to query the information about the WAF instance within your Alibaba Cloud account. The information includes the ID, version, status, and expiration time of the instance.
        
        @param request: DescribeInstanceInfoRequest
        @return: DescribeInstanceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_info_with_options_async(request, runtime)

    def describe_instance_spec_info_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceSpecInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse:
        """
        @param request: DescribeInstanceSpecInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSpecInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecInfo',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_instance_spec_info_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceSpecInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse:
        """
        @param request: DescribeInstanceSpecInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInstanceSpecInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstanceSpecInfo',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_instance_spec_info(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceSpecInfoRequest,
    ) -> waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse:
        """
        @param request: DescribeInstanceSpecInfoRequest
        @return: DescribeInstanceSpecInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_spec_info_with_options(request, runtime)

    async def describe_instance_spec_info_async(
        self,
        request: waf_openapi_20190910_models.DescribeInstanceSpecInfoRequest,
    ) -> waf_openapi_20190910_models.DescribeInstanceSpecInfoResponse:
        """
        @param request: DescribeInstanceSpecInfoRequest
        @return: DescribeInstanceSpecInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_instance_spec_info_with_options_async(request, runtime)

    def describe_log_service_status_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeLogServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeLogServiceStatusResponse:
        """
        @param request: DescribeLogServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogServiceStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeLogServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_service_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeLogServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeLogServiceStatusResponse:
        """
        @param request: DescribeLogServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeLogServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLogServiceStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeLogServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_service_status(
        self,
        request: waf_openapi_20190910_models.DescribeLogServiceStatusRequest,
    ) -> waf_openapi_20190910_models.DescribeLogServiceStatusResponse:
        """
        @param request: DescribeLogServiceStatusRequest
        @return: DescribeLogServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_log_service_status_with_options(request, runtime)

    async def describe_log_service_status_async(
        self,
        request: waf_openapi_20190910_models.DescribeLogServiceStatusRequest,
    ) -> waf_openapi_20190910_models.DescribeLogServiceStatusResponse:
        """
        @param request: DescribeLogServiceStatusRequest
        @return: DescribeLogServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_log_service_status_with_options_async(request, runtime)

    def describe_protection_module_code_config_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigResponse:
        """
        @param request: DescribeProtectionModuleCodeConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtectionModuleCodeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code_type):
            query['CodeType'] = request.code_type
        if not UtilClient.is_unset(request.code_value):
            query['CodeValue'] = request.code_value
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtectionModuleCodeConfig',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_protection_module_code_config_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigResponse:
        """
        @param request: DescribeProtectionModuleCodeConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtectionModuleCodeConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.code_type):
            query['CodeType'] = request.code_type
        if not UtilClient.is_unset(request.code_value):
            query['CodeValue'] = request.code_value
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtectionModuleCodeConfig',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_protection_module_code_config(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigResponse:
        """
        @param request: DescribeProtectionModuleCodeConfigRequest
        @return: DescribeProtectionModuleCodeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_code_config_with_options(request, runtime)

    async def describe_protection_module_code_config_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleCodeConfigResponse:
        """
        @param request: DescribeProtectionModuleCodeConfigRequest
        @return: DescribeProtectionModuleCodeConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_protection_module_code_config_with_options_async(request, runtime)

    def describe_protection_module_mode_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleModeResponse:
        """
        @param request: DescribeProtectionModuleModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtectionModuleModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtectionModuleMode',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_protection_module_mode_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleModeResponse:
        """
        @param request: DescribeProtectionModuleModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtectionModuleModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtectionModuleMode',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_protection_module_mode(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleModeRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleModeResponse:
        """
        @param request: DescribeProtectionModuleModeRequest
        @return: DescribeProtectionModuleModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_mode_with_options(request, runtime)

    async def describe_protection_module_mode_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleModeRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleModeResponse:
        """
        @param request: DescribeProtectionModuleModeRequest
        @return: DescribeProtectionModuleModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_protection_module_mode_with_options_async(request, runtime)

    def describe_protection_module_rules_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse:
        """
        @param request: DescribeProtectionModuleRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtectionModuleRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtectionModuleRules',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_protection_module_rules_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse:
        """
        @param request: DescribeProtectionModuleRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtectionModuleRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtectionModuleRules',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_protection_module_rules(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleRulesRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse:
        """
        @param request: DescribeProtectionModuleRulesRequest
        @return: DescribeProtectionModuleRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_rules_with_options(request, runtime)

    async def describe_protection_module_rules_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleRulesRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleRulesResponse:
        """
        @param request: DescribeProtectionModuleRulesRequest
        @return: DescribeProtectionModuleRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_protection_module_rules_with_options_async(request, runtime)

    def describe_protection_module_status_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse:
        """
        @param request: DescribeProtectionModuleStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtectionModuleStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtectionModuleStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_protection_module_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse:
        """
        @param request: DescribeProtectionModuleStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProtectionModuleStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProtectionModuleStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_protection_module_status(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleStatusRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse:
        """
        @param request: DescribeProtectionModuleStatusRequest
        @return: DescribeProtectionModuleStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_protection_module_status_with_options(request, runtime)

    async def describe_protection_module_status_async(
        self,
        request: waf_openapi_20190910_models.DescribeProtectionModuleStatusRequest,
    ) -> waf_openapi_20190910_models.DescribeProtectionModuleStatusResponse:
        """
        @param request: DescribeProtectionModuleStatusRequest
        @return: DescribeProtectionModuleStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_protection_module_status_with_options_async(request, runtime)

    def describe_rule_groups_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeRuleGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeRuleGroupsResponse:
        """
        @param request: DescribeRuleGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.waf_lang):
            query['WafLang'] = request.waf_lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleGroups',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeRuleGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rule_groups_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeRuleGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeRuleGroupsResponse:
        """
        @param request: DescribeRuleGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRuleGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.waf_lang):
            query['WafLang'] = request.waf_lang
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleGroups',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeRuleGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rule_groups(
        self,
        request: waf_openapi_20190910_models.DescribeRuleGroupsRequest,
    ) -> waf_openapi_20190910_models.DescribeRuleGroupsResponse:
        """
        @param request: DescribeRuleGroupsRequest
        @return: DescribeRuleGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_groups_with_options(request, runtime)

    async def describe_rule_groups_async(
        self,
        request: waf_openapi_20190910_models.DescribeRuleGroupsRequest,
    ) -> waf_openapi_20190910_models.DescribeRuleGroupsResponse:
        """
        @param request: DescribeRuleGroupsRequest
        @return: DescribeRuleGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rule_groups_with_options_async(request, runtime)

    def describe_rules_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeRulesResponse:
        """
        @param request: DescribeRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_type):
            query['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.cve_id_key):
            query['CveIdKey'] = request.cve_id_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protection_type):
            query['ProtectionType'] = request.protection_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.rule_group_id):
            query['RuleGroupId'] = request.rule_group_id
        if not UtilClient.is_unset(request.rule_id_key):
            query['RuleIdKey'] = request.rule_id_key
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRules',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rules_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeRulesResponse:
        """
        @param request: DescribeRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_type):
            query['ApplicationType'] = request.application_type
        if not UtilClient.is_unset(request.cve_id_key):
            query['CveIdKey'] = request.cve_id_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protection_type):
            query['ProtectionType'] = request.protection_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.risk_level):
            query['RiskLevel'] = request.risk_level
        if not UtilClient.is_unset(request.rule_group_id):
            query['RuleGroupId'] = request.rule_group_id
        if not UtilClient.is_unset(request.rule_id_key):
            query['RuleIdKey'] = request.rule_id_key
        if not UtilClient.is_unset(request.source_ip):
            query['SourceIp'] = request.source_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRules',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rules(
        self,
        request: waf_openapi_20190910_models.DescribeRulesRequest,
    ) -> waf_openapi_20190910_models.DescribeRulesResponse:
        """
        @param request: DescribeRulesRequest
        @return: DescribeRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_rules_with_options(request, runtime)

    async def describe_rules_async(
        self,
        request: waf_openapi_20190910_models.DescribeRulesRequest,
    ) -> waf_openapi_20190910_models.DescribeRulesResponse:
        """
        @param request: DescribeRulesRequest
        @return: DescribeRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_rules_with_options_async(request, runtime)

    def describe_waf_source_ip_segment_with_options(
        self,
        request: waf_openapi_20190910_models.DescribeWafSourceIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse:
        """
        @param request: DescribeWafSourceIpSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWafSourceIpSegmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWafSourceIpSegment',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_waf_source_ip_segment_with_options_async(
        self,
        request: waf_openapi_20190910_models.DescribeWafSourceIpSegmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse:
        """
        @param request: DescribeWafSourceIpSegmentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWafSourceIpSegmentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWafSourceIpSegment',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_waf_source_ip_segment(
        self,
        request: waf_openapi_20190910_models.DescribeWafSourceIpSegmentRequest,
    ) -> waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse:
        """
        @param request: DescribeWafSourceIpSegmentRequest
        @return: DescribeWafSourceIpSegmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_waf_source_ip_segment_with_options(request, runtime)

    async def describe_waf_source_ip_segment_async(
        self,
        request: waf_openapi_20190910_models.DescribeWafSourceIpSegmentRequest,
    ) -> waf_openapi_20190910_models.DescribeWafSourceIpSegmentResponse:
        """
        @param request: DescribeWafSourceIpSegmentRequest
        @return: DescribeWafSourceIpSegmentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_waf_source_ip_segment_with_options_async(request, runtime)

    def modify_domain_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyDomainResponse:
        """
        @summary Modifies the configurations of a domain name.
        
        @param request: ModifyDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_header_mode):
            query['AccessHeaderMode'] = request.access_header_mode
        if not UtilClient.is_unset(request.access_headers):
            query['AccessHeaders'] = request.access_headers
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.cloud_native_instances):
            query['CloudNativeInstances'] = request.cloud_native_instances
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.connection_time):
            query['ConnectionTime'] = request.connection_time
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.http_2port):
            query['Http2Port'] = request.http_2port
        if not UtilClient.is_unset(request.http_port):
            query['HttpPort'] = request.http_port
        if not UtilClient.is_unset(request.http_to_user_ip):
            query['HttpToUserIp'] = request.http_to_user_ip
        if not UtilClient.is_unset(request.https_port):
            query['HttpsPort'] = request.https_port
        if not UtilClient.is_unset(request.https_redirect):
            query['HttpsRedirect'] = request.https_redirect
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_follow_status):
            query['IpFollowStatus'] = request.ip_follow_status
        if not UtilClient.is_unset(request.is_access_product):
            query['IsAccessProduct'] = request.is_access_product
        if not UtilClient.is_unset(request.keepalive):
            query['Keepalive'] = request.keepalive
        if not UtilClient.is_unset(request.keepalive_requests):
            query['KeepaliveRequests'] = request.keepalive_requests
        if not UtilClient.is_unset(request.keepalive_timeout):
            query['KeepaliveTimeout'] = request.keepalive_timeout
        if not UtilClient.is_unset(request.load_balancing):
            query['LoadBalancing'] = request.load_balancing
        if not UtilClient.is_unset(request.log_headers):
            query['LogHeaders'] = request.log_headers
        if not UtilClient.is_unset(request.read_time):
            query['ReadTime'] = request.read_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retry):
            query['Retry'] = request.retry
        if not UtilClient.is_unset(request.sni_host):
            query['SniHost'] = request.sni_host
        if not UtilClient.is_unset(request.sni_status):
            query['SniStatus'] = request.sni_status
        if not UtilClient.is_unset(request.source_ips):
            query['SourceIps'] = request.source_ips
        if not UtilClient.is_unset(request.write_time):
            query['WriteTime'] = request.write_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyDomainResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyDomainRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyDomainResponse:
        """
        @summary Modifies the configurations of a domain name.
        
        @param request: ModifyDomainRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDomainResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_header_mode):
            query['AccessHeaderMode'] = request.access_header_mode
        if not UtilClient.is_unset(request.access_headers):
            query['AccessHeaders'] = request.access_headers
        if not UtilClient.is_unset(request.access_type):
            query['AccessType'] = request.access_type
        if not UtilClient.is_unset(request.cloud_native_instances):
            query['CloudNativeInstances'] = request.cloud_native_instances
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.connection_time):
            query['ConnectionTime'] = request.connection_time
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.http_2port):
            query['Http2Port'] = request.http_2port
        if not UtilClient.is_unset(request.http_port):
            query['HttpPort'] = request.http_port
        if not UtilClient.is_unset(request.http_to_user_ip):
            query['HttpToUserIp'] = request.http_to_user_ip
        if not UtilClient.is_unset(request.https_port):
            query['HttpsPort'] = request.https_port
        if not UtilClient.is_unset(request.https_redirect):
            query['HttpsRedirect'] = request.https_redirect
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ip_follow_status):
            query['IpFollowStatus'] = request.ip_follow_status
        if not UtilClient.is_unset(request.is_access_product):
            query['IsAccessProduct'] = request.is_access_product
        if not UtilClient.is_unset(request.keepalive):
            query['Keepalive'] = request.keepalive
        if not UtilClient.is_unset(request.keepalive_requests):
            query['KeepaliveRequests'] = request.keepalive_requests
        if not UtilClient.is_unset(request.keepalive_timeout):
            query['KeepaliveTimeout'] = request.keepalive_timeout
        if not UtilClient.is_unset(request.load_balancing):
            query['LoadBalancing'] = request.load_balancing
        if not UtilClient.is_unset(request.log_headers):
            query['LogHeaders'] = request.log_headers
        if not UtilClient.is_unset(request.read_time):
            query['ReadTime'] = request.read_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retry):
            query['Retry'] = request.retry
        if not UtilClient.is_unset(request.sni_host):
            query['SniHost'] = request.sni_host
        if not UtilClient.is_unset(request.sni_status):
            query['SniStatus'] = request.sni_status
        if not UtilClient.is_unset(request.source_ips):
            query['SourceIps'] = request.source_ips
        if not UtilClient.is_unset(request.write_time):
            query['WriteTime'] = request.write_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomain',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyDomainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain(
        self,
        request: waf_openapi_20190910_models.ModifyDomainRequest,
    ) -> waf_openapi_20190910_models.ModifyDomainResponse:
        """
        @summary Modifies the configurations of a domain name.
        
        @param request: ModifyDomainRequest
        @return: ModifyDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_with_options(request, runtime)

    async def modify_domain_async(
        self,
        request: waf_openapi_20190910_models.ModifyDomainRequest,
    ) -> waf_openapi_20190910_models.ModifyDomainResponse:
        """
        @summary Modifies the configurations of a domain name.
        
        @param request: ModifyDomainRequest
        @return: ModifyDomainResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_with_options_async(request, runtime)

    def modify_domain_ipv_6status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyDomainIpv6StatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse:
        """
        @param request: ModifyDomainIpv6StatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDomainIpv6StatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainIpv6Status',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_domain_ipv_6status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyDomainIpv6StatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse:
        """
        @param request: ModifyDomainIpv6StatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDomainIpv6StatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDomainIpv6Status',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_domain_ipv_6status(
        self,
        request: waf_openapi_20190910_models.ModifyDomainIpv6StatusRequest,
    ) -> waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse:
        """
        @param request: ModifyDomainIpv6StatusRequest
        @return: ModifyDomainIpv6StatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_domain_ipv_6status_with_options(request, runtime)

    async def modify_domain_ipv_6status_async(
        self,
        request: waf_openapi_20190910_models.ModifyDomainIpv6StatusRequest,
    ) -> waf_openapi_20190910_models.ModifyDomainIpv6StatusResponse:
        """
        @param request: ModifyDomainIpv6StatusRequest
        @return: ModifyDomainIpv6StatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_domain_ipv_6status_with_options_async(request, runtime)

    def modify_log_retrieval_status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyLogRetrievalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse:
        """
        @param request: ModifyLogRetrievalStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLogRetrievalStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogRetrievalStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_log_retrieval_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyLogRetrievalStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse:
        """
        @param request: ModifyLogRetrievalStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLogRetrievalStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogRetrievalStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_log_retrieval_status(
        self,
        request: waf_openapi_20190910_models.ModifyLogRetrievalStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse:
        """
        @param request: ModifyLogRetrievalStatusRequest
        @return: ModifyLogRetrievalStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_log_retrieval_status_with_options(request, runtime)

    async def modify_log_retrieval_status_async(
        self,
        request: waf_openapi_20190910_models.ModifyLogRetrievalStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyLogRetrievalStatusResponse:
        """
        @param request: ModifyLogRetrievalStatusRequest
        @return: ModifyLogRetrievalStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_log_retrieval_status_with_options_async(request, runtime)

    def modify_log_service_status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyLogServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyLogServiceStatusResponse:
        """
        @param request: ModifyLogServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLogServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogServiceStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyLogServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_log_service_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyLogServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyLogServiceStatusResponse:
        """
        @param request: ModifyLogServiceStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyLogServiceStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLogServiceStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyLogServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_log_service_status(
        self,
        request: waf_openapi_20190910_models.ModifyLogServiceStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyLogServiceStatusResponse:
        """
        @param request: ModifyLogServiceStatusRequest
        @return: ModifyLogServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_log_service_status_with_options(request, runtime)

    async def modify_log_service_status_async(
        self,
        request: waf_openapi_20190910_models.ModifyLogServiceStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyLogServiceStatusResponse:
        """
        @param request: ModifyLogServiceStatusRequest
        @return: ModifyLogServiceStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_log_service_status_with_options_async(request, runtime)

    def modify_protection_module_mode_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleModeResponse:
        """
        @param request: ModifyProtectionModuleModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtectionModuleModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtectionModuleMode',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_protection_module_mode_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleModeResponse:
        """
        @param request: ModifyProtectionModuleModeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtectionModuleModeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtectionModuleMode',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_protection_module_mode(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleModeRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleModeResponse:
        """
        @param request: ModifyProtectionModuleModeRequest
        @return: ModifyProtectionModuleModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_mode_with_options(request, runtime)

    async def modify_protection_module_mode_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleModeRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleModeResponse:
        """
        @param request: ModifyProtectionModuleModeRequest
        @return: ModifyProtectionModuleModeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_module_mode_with_options_async(request, runtime)

    def modify_protection_module_rule_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse:
        """
        @param request: ModifyProtectionModuleRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtectionModuleRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lock_version):
            query['LockVersion'] = request.lock_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtectionModuleRule',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_protection_module_rule_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse:
        """
        @param request: ModifyProtectionModuleRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtectionModuleRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lock_version):
            query['LockVersion'] = request.lock_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtectionModuleRule',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_protection_module_rule(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse:
        """
        @param request: ModifyProtectionModuleRuleRequest
        @return: ModifyProtectionModuleRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_rule_with_options(request, runtime)

    async def modify_protection_module_rule_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleRuleRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleRuleResponse:
        """
        @param request: ModifyProtectionModuleRuleRequest
        @return: ModifyProtectionModuleRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_module_rule_with_options_async(request, runtime)

    def modify_protection_module_status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse:
        """
        @param request: ModifyProtectionModuleStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtectionModuleStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_status):
            query['ModuleStatus'] = request.module_status
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtectionModuleStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_protection_module_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse:
        """
        @param request: ModifyProtectionModuleStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtectionModuleStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.module_status):
            query['ModuleStatus'] = request.module_status
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtectionModuleStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_protection_module_status(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse:
        """
        @param request: ModifyProtectionModuleStatusRequest
        @return: ModifyProtectionModuleStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_module_status_with_options(request, runtime)

    async def modify_protection_module_status_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionModuleStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionModuleStatusResponse:
        """
        @param request: ModifyProtectionModuleStatusRequest
        @return: ModifyProtectionModuleStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_module_status_with_options_async(request, runtime)

    def modify_protection_rule_cache_status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse:
        """
        @param request: ModifyProtectionRuleCacheStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtectionRuleCacheStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtectionRuleCacheStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_protection_rule_cache_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse:
        """
        @param request: ModifyProtectionRuleCacheStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtectionRuleCacheStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtectionRuleCacheStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_protection_rule_cache_status(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse:
        """
        @param request: ModifyProtectionRuleCacheStatusRequest
        @return: ModifyProtectionRuleCacheStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_cache_status_with_options(request, runtime)

    async def modify_protection_rule_cache_status_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleCacheStatusResponse:
        """
        @param request: ModifyProtectionRuleCacheStatusRequest
        @return: ModifyProtectionRuleCacheStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_rule_cache_status_with_options_async(request, runtime)

    def modify_protection_rule_status_with_options(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse:
        """
        @param request: ModifyProtectionRuleStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtectionRuleStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lock_version):
            query['LockVersion'] = request.lock_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_status):
            query['RuleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtectionRuleStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_protection_rule_status_with_options_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse:
        """
        @param request: ModifyProtectionRuleStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyProtectionRuleStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.defense_type):
            query['DefenseType'] = request.defense_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lock_version):
            query['LockVersion'] = request.lock_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_status):
            query['RuleStatus'] = request.rule_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyProtectionRuleStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_protection_rule_status(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse:
        """
        @param request: ModifyProtectionRuleStatusRequest
        @return: ModifyProtectionRuleStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_protection_rule_status_with_options(request, runtime)

    async def modify_protection_rule_status_async(
        self,
        request: waf_openapi_20190910_models.ModifyProtectionRuleStatusRequest,
    ) -> waf_openapi_20190910_models.ModifyProtectionRuleStatusResponse:
        """
        @param request: ModifyProtectionRuleStatusRequest
        @return: ModifyProtectionRuleStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_protection_rule_status_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: waf_openapi_20190910_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.MoveResourceGroupResponse:
        """
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: waf_openapi_20190910_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.MoveResourceGroupResponse:
        """
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: waf_openapi_20190910_models.MoveResourceGroupRequest,
    ) -> waf_openapi_20190910_models.MoveResourceGroupResponse:
        """
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: waf_openapi_20190910_models.MoveResourceGroupRequest,
    ) -> waf_openapi_20190910_models.MoveResourceGroupResponse:
        """
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def set_domain_rule_group_with_options(
        self,
        request: waf_openapi_20190910_models.SetDomainRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.SetDomainRuleGroupResponse:
        """
        @param request: SetDomainRuleGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDomainRuleGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_group_id):
            query['RuleGroupId'] = request.rule_group_id
        if not UtilClient.is_unset(request.waf_ai_status):
            query['WafAiStatus'] = request.waf_ai_status
        if not UtilClient.is_unset(request.waf_version):
            query['WafVersion'] = request.waf_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainRuleGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.SetDomainRuleGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_domain_rule_group_with_options_async(
        self,
        request: waf_openapi_20190910_models.SetDomainRuleGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> waf_openapi_20190910_models.SetDomainRuleGroupResponse:
        """
        @param request: SetDomainRuleGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetDomainRuleGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domains):
            query['Domains'] = request.domains
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_group_id):
            query['RuleGroupId'] = request.rule_group_id
        if not UtilClient.is_unset(request.waf_ai_status):
            query['WafAiStatus'] = request.waf_ai_status
        if not UtilClient.is_unset(request.waf_version):
            query['WafVersion'] = request.waf_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainRuleGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            waf_openapi_20190910_models.SetDomainRuleGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_domain_rule_group(
        self,
        request: waf_openapi_20190910_models.SetDomainRuleGroupRequest,
    ) -> waf_openapi_20190910_models.SetDomainRuleGroupResponse:
        """
        @param request: SetDomainRuleGroupRequest
        @return: SetDomainRuleGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_domain_rule_group_with_options(request, runtime)

    async def set_domain_rule_group_async(
        self,
        request: waf_openapi_20190910_models.SetDomainRuleGroupRequest,
    ) -> waf_openapi_20190910_models.SetDomainRuleGroupResponse:
        """
        @param request: SetDomainRuleGroupRequest
        @return: SetDomainRuleGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_domain_rule_group_with_options_async(request, runtime)
